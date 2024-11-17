[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org) ![user](https://img.shields.io/badge/GoogleColab-grey?style=flat&logo=googlecolab) ![user](https://img.shields.io/badge/Chemodeling-App-yellow?) ![user](https://img.shields.io/badge/Userfriend-1.0-sgreen?) 


# S∈∈R: Gas Phase Molecular Charge State Predictor


<br /><img align = "center" width="700" alt="focus" src="https://github.com/user-attachments/assets/917ed8d7-1fee-4ec8-b81c-546e331edf75">
<br />
<br />
#
### **Introduction**
S∈∈R (**S**tate **E**nsemble **E**nergy **R**ecognition) is a hybrid knowledge-based machine learning program for ranking molecular charge sites and subsequent prediction of a gas phase major equilibrium charge state. The objective of S∈∈R is to accurately assign a minimum energy charge state (with residually higher energy ranked candidate charge states available as auxiliary models) for a given molecule so as to effectively eliminate gross workload and computational cost that can arise from charge modeling any system with numerous titratable sites. This program is appropriate for modeling mass spectrometry $[M-H]^-$ and $[M+H]^+$ charge modes.

The ensembles of molecular ions used to train S∈∈R have been geometry optimized using the quantum mechanical density functional theory D3BJ-B3LYP/6-31G(d,p) or D3BJ-B3LYP/6-31+G(d,p). The accuracy of our previously predicted gas phase molecular ions (used in the training) was asssessed and screened by comparing computed collision cross section values against experimental ion mobility mass spectrometry reference values. 

#
### **Benefits**
-  High turnaround time
-  Unambiguous results
-  Good generalizability
-  Competitive accuracy
-  No structural artifacts
-  User-friendly interface
-  Seemless workflow integration

#
### **Specifications**
Currently, S∈∈R supports biomolecules and small molecules with commonly observed oxygen and nitrogen as the proton donating or proton acccepting atoms. 

Although the ANI-2x geometry optimization use in S∈∈R supports only the atom types H, C, N, O, F, Cl, and S, we run surrogate-optimization for the atom types P, Se, Br, and I to extend S∈∈R applicability to systems containing these atoms.

#
### **Functionalities**

-    Rank charge sites
-    Predict equilibrium charge state
-    Auto generate $[M+H]^+$ or  $[M-H]^-$ structure
-    Soft geometry optimization
-    Compute model relative energy score

#
### **Requirements**
Access to Google Colab is required to run S∈∈R in its intended form. A neutral molecule input file must be in xyz format (see the Additional Information section).

#
### **Additional Information**
#### Input xyz file format:
```twig
32               <--- number of atoms
Adenosine        <--- system name
C          0.99780        0.54800        0.55510    
N          0.50730       -0.59360        0.05790
C         -0.81000       -0.67980       -0.21870
C         -1.63810        0.44290        0.02080
C         -0.97870        1.58660        0.54380
N          0.34920        1.68350        0.83200
N         -1.95520        2.54830        0.68610
C         -3.12290        1.92820        0.28910
N         -2.99430        0.69750       -0.13430
C         -1.76470        3.92500        1.24140
C         -0.69150        4.70330        0.43840
C         -1.45460        5.92710       -0.04840
C         -2.88530        5.38690       -0.11800
O         -2.97540        4.60630        1.06550
C         -4.03200        6.41380       -0.17650
O         -3.81480        7.50930        0.69290
O         -0.95000        6.36360       -1.29830
O          0.39650        5.14920        1.22310
...
```

#### S∈∈R output xyz file for $[M+H]^+$:
```twig
33                   <--- number of atoms
model_energy_-963.90 <--- state energy
C          1.05953          0.66186          0.43596
N          0.52345         -0.51138         -0.04995
H          1.15112         -1.27216         -0.28706
C         -0.82830         -0.63465         -0.30184
C         -1.59541          0.47619         -0.01025
C         -0.94599          1.60849          0.46715
N          0.38790          1.73564          0.69982
N         -1.92473          2.55063          0.65226
C         -3.10928          1.92333          0.30223
N         -2.96391          0.69732         -0.10316
C         -1.77957          3.91399          1.17078
C         -0.73075          4.75616          0.41687
C         -1.52082          5.96647         -0.07566
C         -2.93187          5.39797         -0.14912
O         -3.01393          4.57743          1.02142
C         -4.05373          6.40627         -0.15382
O         -3.77147          7.42167          0.78567
O         -1.01295          6.42594         -1.30962
...
```


#
### Accessibility
 [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">]() <code style="color : grey">access the S∈∈R platform is pending publication</code>
<br />

#
### **Limitation**
Titratable sites for protonation or deprotonation are limited to nitrogen and oxygen; all other atom types are completely neglected. 

#
### **Disclaimer and Remarks**
All data used in this ML model development was generated inhouse. We do not intend to make publically available any original quantum mechanical data pertaining to the DFT geometry optimization and single point energy calculation, unless reasonably requested. S∈∈R results may differ significantly from pKa-based methods since 1) pKa is not considered in the training and 2) the target is gas phase.


Although only "soft" geometry optimization is carried out, it is a best practice and recommended that an input structure and an output structure be visually compared to ensure that the original molecular integrity, other than a change at the protonation or deprotonation site, is preserved.  

#
### Acknowledgement 
-   [Merz research group](https://github.com/merzlab) 

-   Quantum mechanical calculations and data used in building this model were organically generated through computational resources and services provided by the Institute for Cyber-Enabled Research [(ICER)](https://github.com/MSU-iCER) at Michigan State University.

<br/>
<br/>

<br />
