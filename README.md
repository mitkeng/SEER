[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org) ![user](https://img.shields.io/badge/GoogleColab-grey?style=flat&logo=googlecolab) ![user](https://img.shields.io/badge/Chemodeling-App-yellow?) ![user](https://img.shields.io/badge/Userfriend-1.0-sgreen?) 


# S∈∈R: Gas Phase Molecular Charge State Predictor


<br /><img align = "center" width="700" alt="focus" src="https://github.com/user-attachments/assets/917ed8d7-1fee-4ec8-b81c-546e331edf75">
<br />
<br />
#
### **Introduction**
S∈∈R (Site Ensemble Energy Recognition) is a hybrid knowledge-based machine learning program for ranking molecular charge sites and subsequent prediction of the gas phase major equilibrium charge state. The objective of S∈∈R is to accurately predict a favorable charge state (with residual ranked candidate charge states available as auxiliary) for a given molecule so as to effectively eliminate gross workload and computational cost that goes into charge modeling any system with numerous titratable sites. This program is appropriate for modeling mass spectrometry $[M-H]^-$ and $[M+H]^+$ charge modes.

The ensembles of molecular ions used to train S∈∈R have been geometry optimized using the quantum mechanical density functional theory D3BJ-B3LYP/6-31G(d,p) or D3BJ-B3LYP/6-31+G(d,p). The accuracy of our previously predicted gas phase molecular ions (used in the training) were asssessed and screened by comparing their computed collision cross section values against experimental (ion mobility mass spetrometry) reference values. 

The S∈∈R advantages include high results turnaround time, good generalizability, competitive accuracy, and an exceptional user-friendly interface within the chemical modeling niche. Additionally, S∈∈R can be seemlessly integrated into a larger *in silico* workflow.

#
### **Specifications**
Currently, S∈∈R supports only oxygen and nitrogen as the proton donating or proton acccepting atoms, thus protonation or deprotonation elsewhere is completely absent in training. Although the ANI-2x geometry optimization use in S∈∈R supports only the atom types H, C, N, O, F, Cl, and S, we run surrogate-optimization for the atom types P, Se, Br, and I to extend S∈∈R applicability to systems with these atoms.

#
### **Functionalities**

-   #### Rank charge sites
-   #### Predict equilibrium charge state
-   #### Auto generate $[M+H]^+$ or  $[M-H]^-$ structure
-   #### Superficial geometry optimization
-   #### Compute model relative energy score

#
### **Requirements**
Access to Google Colab is required to run S∈∈R in its intended form. 

#
### **Additional Information**
#### Input xyz file format:
```twig
32               <--- number of atoms
Adenosine        <--- description
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
33                  <--- number of atoms
Adenosine_rank1     <--- description
C             1.0595366700000           0.6618670200000           0.4359603600000
N             0.5234542000000          -0.5113856000000          -0.0499514900000
H             1.1511237200000          -1.2721655500000          -0.2870695500000
C            -0.8283053300000          -0.6346559700000          -0.3018468200000
C            -1.5954153200000           0.4761918900000          -0.0102557000000
C            -0.9459964300000           1.6084947600000           0.4671549600000
N             0.3879043500000           1.7356407900000           0.6998270300000
N            -1.9247334500000           2.5506385400000           0.6522635200000
C            -3.1092849900000           1.9233388500000           0.3022350500000
N            -2.9639190400000           0.6973210700000          -0.1031672500000
C            -1.7795772700000           3.9139998700000           1.1707870200000
C            -0.7307526100000           4.7561683500000           0.4168727900000
C            -1.5208278300000           5.9664717700000          -0.0756643500000
C            -2.9318730100000           5.3979711500000          -0.1491259600000
O            -3.0139376200000           4.5774311700000           1.0214234700000
C            -4.0537368600000           6.4062715300000          -0.1538259900000
O            -3.7714783600000           7.4216773200000           0.7856745300000
O            -1.0129584200000           6.4259498300000          -1.3096238200000
...
```

#
### **Disclaimer and Remarks**
All data use in this ML model development was generated inhouse. It is a best practice and recommended that an input structure and an output structure be visually compared to ensure that the original molecular integrity, other than the protonation or deprotonation site, is preserved.  

#
### Acknowledgement 
-   [Merz research group](https://github.com/merzlab) 

-   Quantum mechanical calculations and data used in building this model were organically generated through computational resources and services provided by the Institute for Cyber-Enabled Research [(ICER)](https://github.com/MSU-iCER) at Michigan State University.

<br/>
<br/>

<br />
