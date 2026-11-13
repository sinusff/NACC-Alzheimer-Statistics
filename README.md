# Multimodal Statistical Analysis of Alzheimer's Disease Progression (NACC Cohort)

Official term project for the **Introductory Statistics Course (Fall 1405)**

---

## Project Overview
This repository hosts a reproducible, multimodal statistical investigation into the anatomical and neuropsychological hallmarks of Alzheimer's disease. Using cross-sectional data from the **National Alzheimer's Coordinating Center (NACC)**, the project examines the predictive and associative power of structural brain MRI biomarkers (Entorhinal cortex volume and cortical thickness) against clinical cognitive diagnostic stages (`Normal`, `MCI`, and `Dementia`).

Detailed project scope, target population, variables, hypotheses, and analytical constraints are formally documented in [`PROJECT_CARD.md`](./PROJECT_CARD.md).

---

## Repository Architecture
The repository strictly complies with the standardized course directory hierarchy:

```text
├── README.md                          # Repository documentation and reproduction guide
├── PROJECT_CARD.md                    # Official project charter and statistical definitions
├── requirements.txt                   # Python software dependencies
├── .gitignore                         # Data protection rules preventing raw data tracking
├── data/
│   ├── README.md                      # Provenance, variable schema, and data audit logs
│   ├── mriscanclean.csv               # (Local only) Structural T1-weighted MRI morphometry
│   ├── udslong_imputed.csv            # (Local only) Clinical, cognitive, and demographic data
│   └── combined_adjacency_matrix.csv  # (Local only) 62-region anatomical cortical connectome
├── src/
│   ├── check_join_flow.py             # Multimodal 1-to-1 matching and attrition verification
│   ├── calc_center_spread.py          # Parametric and non-parametric summary statistics engine
│   ├── phase1_plots.py                # Visual distribution pipeline producing publication figures
│   └── phase1_j5_summary.py           # Joint bivariate cognitive-morphometry modeling script
├── notebooks/
│   ├── phase1_exploration.py          # Initial exploratory data interrogation script
│   └── calc_exact_stats.py            # Verification script for exact counts and quantiles
├── figures/
│   ├── fig1_diagnosis_dist.png        # Bar distribution of cognitive diagnoses
│   ├── fig2_moca_dist.png             # Histogram with KDE of MoCA cognitive score
│   ├── fig3_volume_dist.png           # Bell-shaped distribution of left entorhinal volume
│   ├── fig4_vol_vs_moca.png           # Bivariate scatter of brain volume vs. MoCA by group
│   └── fig5_joint_summary.png         # Joint distribution plot with regression fit and marginals
└── reports/
    ├── phase1/                        # Phase 1 technical deliverables
    ├── phase2/                        # Phase 2 probabilistic analysis
    ├── phase3/                        # Phase 3 inferential statistics & bootstrapping
    ├── phase4/                        # Phase 4 linear regression modeling
    └── phase5(final)/                 # Integrated final thesis and sensitivity analysis