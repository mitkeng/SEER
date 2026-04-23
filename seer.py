import os
import sys
import argparse
import shutil
import math
import re
import pandas as pd
import numpy as np
import ydf
import ase
import torchani
from openbabel import pybel
from ase.io import read, write
from ase.optimize import LBFGS
from pymol import cmd

def get_en_com(atoms, atomic_EN):
    m_x, m_y, m_z, total_en = 0, 0, 0, 0
    for atom in atoms:
        en = atomic_EN.get(atom.symbol, 2.5)
        pos = atom.position
        m_x += en * pos[0]
        m_y += en * pos[1]
        m_z += en * pos[2]
        total_en += en
    return (m_x/total_en, m_y/total_en, m_z/total_en)

def find_angle(p_coord, coe, com):
    ab = (coe[0]-p_coord[0], coe[1]-p_coord[1], coe[2]-p_coord[2])
    bc = (p_coord[0]-com[0], p_coord[1]-com[1], p_coord[2]-com[2])
    dot = ab[0]*bc[0] + ab[1]*bc[1] + ab[2]*bc[2]
    mag_ab = math.sqrt(sum(x**2 for x in ab))
    mag_bc = math.sqrt(sum(x**2 for x in bc))
    return math.acos(dot/(mag_ab*mag_bc)) * (180/math.pi)

def new_proton_coord(site_symbol, pos, angle_inc=10, act=0):
    x, y, z = pos
    r = 0.95 if site_symbol == "O" else 1.0
    theta = math.acos(0) + (70 + angle_inc) * (math.pi/180)
    phi = 0.10 - math.sin(theta/(angle_inc*0.01+.01)) if act == 0 else 0.10 + math.cos(theta/act)
    return [r*math.sin(theta)*math.cos(phi)+x, r*math.sin(theta)*math.sin(phi)+y, r*math.cos(theta)+z]

def run_seer(smile, mol_name, mode):
    print(f"--- Executing Full SEER Workflow: {mol_name} ({mode}) ---")
    atomic_EN = {'C':2.55, 'O':3.44, 'H':2.20, 'N':3.04, 'F':3.98, 'Cl':3.16, 'Br':2.96, 'I':2.66, 'S':2.58, 'P':3.15, 'Se':2.55}
    atomic_pol = {'O':5.3, 'N':7.4, 'S':19.4, 'P':25, 'Se':29}

    res_dir = f'Completed_Job/{mol_name}'
    os.makedirs(res_dir, exist_ok=True)

    mol = pybel.readstring('smi', smile)
    mol.addh()
    mol.make3D(forcefield='MMFF94')
    mol.localopt(forcefield='MMFF94', steps=1000)
    mol.write('xyz', os.path.join(res_dir, f'{mol_name}.xyz'), overwrite=True)

    cmd.delete('all')
    cmd.load(os.path.join(res_dir, f'{mol_name}.xyz'))
    cmd.set('dot_solvent', 0)
    cmd.set('dot_density', 2)
    msa = cmd.get_area('all')

    atoms = read(os.path.join(res_dir, f'{mol_name}.xyz'))
    com = atoms.get_center_of_mass()
    coe = get_en_com(atoms, atomic_EN)
    counts = {'O':0, 'N':0, 'Halogen':0, 'Other':0}
    for a in atoms:
        if a.symbol == 'O': counts['O']+=1
        elif a.symbol == 'N': counts['N']+=1
        elif a.symbol in ['F','Cl','Br','I']: counts['Halogen']+=1
        elif a.symbol in ['S','P','Se']: counts['Other']+=1

    sites = [a for a in atoms if a.symbol in ['N', 'O']]
    initial_site_count = len(sites)
    model = ydf.load_model('seer_pos_model' if mode=='[M+H]+' else 'seer_neg_model')
    rmse = 4.95566

    site_data = []
    for s in sites:
        dist_com = sum((s.position[i]-com[i])**2 for i in range(3))
        dist_coe = sum((s.position[i]-coe[i])**2 for i in range(3))
        dist_comcoe = sum((com[i]-coe[i])**2 for i in range(3))
        angle = find_angle(s.position, coe, com)
        feat = [atomic_pol[s.symbol], dist_com, dist_coe, dist_comcoe, angle, msa, counts['O'], counts['N'], counts['Halogen'], counts['Other']]
        site_data.append(feat)

    df = pd.DataFrame(site_data, columns=['Atomic_pol','COM_Dist','COE_Dist','COM2COE_Dist','Interaction_Angle','MSA','Total_O','Total_N','Total_Halogen','Total_Othergen'])
    preds = model.predict(df) / rmse
    df['Predicted_Energy'] = preds

    thresh = max(1, int(round((df['Predicted_Energy'].min() / (df['Predicted_Energy'].var() + df['Predicted_Energy'].std()) + (rmse/3)), 0)))
    best_indices = df.sort_values('Predicted_Energy').index[:thresh]

    calc = torchani.models.ANI2x().ase()
    optimized_results = []
    for i, idx in enumerate(best_indices):
        site = sites[idx]
        p_atoms = atoms.copy()
        p_atoms.append(ase.Atom('H', position=new_proton_coord(site.symbol, site.position)))
        p_atoms.calc = calc
        LBFGS(p_atoms, logfile=None).run(fmax=0.05, steps=50)
        energy = p_atoms.get_potential_energy() * 0.0367493
        fname = f'{mol_name}_opt_{i}.xyz'
        write(os.path.join(res_dir, fname), p_atoms)
        optimized_results.append({'file': fname, 'energy': energy})

    final_sorted = sorted(optimized_results, key=lambda x: x['energy'])
    min_e = final_sorted[0]['energy']
    summary = []
    for i, res in enumerate(final_sorted):
        new_name = f"{mol_name}_Rank{i+1}_model.xyz"
        os.rename(os.path.join(res_dir, res['file']), os.path.join(res_dir, new_name))
        rel_e = (res['energy'] - min_e) * 627.509
        summary.append({'Rank': f'Rank {i+1}', 'Filename': new_name, 'Energy': res['energy'], 'Rel_Energy': rel_e})

    summary_df = pd.DataFrame(summary)
    summary_df.to_csv(os.path.join(res_dir, 'final_ranking_summary.csv'), index=False)

    filtering_summary = f"""Summary of Candidate Filtering for {mol_name}
Initially identified {initial_site_count} potential protonation sites based on topology.
A statistical threshold restricted refinement to the top {len(final_sorted)} candidates.
These finalized models represent the top-tier stable protomers within the defined energy window."""
    with open(os.path.join(res_dir, 'summary.txt'), 'w') as f:
        f.write(filtering_summary)

    print(f"\n--- Final Ranking Summary for {mol_name} ---")
    print(summary_df.to_string(index=False))
    print(f"\n--- Done. Results saved to {res_dir} ---")

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--smiles', required=True)
    p.add_argument('--name', default='mol')
    p.add_argument('--mode', default='[M+H]+')
    args = p.parse_args()
    run_seer(args.smiles, args.name, args.mode)
