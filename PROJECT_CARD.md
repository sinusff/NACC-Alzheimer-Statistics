# Project Card: NACC Multimodal Alzheimer's Statistical Analysis

## 1. Dataset and Subset
- **Selected Path:** Path C: `NACC Alzheimer's Data` (`UDS + MRI Multimodal Path`).
- **Primary Files Used:**
  - `udslong_imputed.csv`: Standardized clinical, neuropsychological, and demographic assessments (`Uniform Data Set - UDS`).
  - `mriscanclean.csv`: Morphometric brain volumetric and cortical thickness measures derived from structural MRI (`FreeSurfer` pipeline).
  - `combined_adjacency_matrix.csv`: Structural cortical adjacency matrix across 62 anatomical regions.
- **Analyzed Subset:** Curated cross-sectional multimodal cohort of exactly 1,237 unique, matched participants ($N = 1,237$) with zero sample attrition across modalities.

## 2. Temporary Project Title
*Statistical Association between Structural Brain Morphometry (MRI) and Clinical Cognitive Status (UDS) in Older Adults: A Multimodal Cross-Sectional Analysis.*

## 3. Main Statistical Question
To what extent are localized structural brain MRI biomarkers (specifically bilateral Entorhinal cortex gray matter volume and cortical thickness) associated with clinical cognitive diagnostic status (`Normal`, `MCI`, and `Dementia`) in older adults evaluated at NACC centers, after statistically controlling for chronological age and educational attainment?

## 4. Unit of Observation and Interpretable Population
- **Unit of Observation:** A single independent human participant at a temporally matched index evaluation visit ($N = 1,237$). Each row represents an individual patient; no repeated or clustered observations exist within the dataset.
- **Interpretable Target Population:** Older adults (aged 50 to 95) presenting to or evaluated at specialized memory clinics and academic Alzheimer's Disease Research Centers (`ADRCs`). Findings are valid within this clinical referral frame of reference and are not directly generalizable to the unselected general population.

## 5. Main Variables and Measurement Scales
- **`NACCUDSD` (Cognitive Diagnosis):** Categorical Ordinal / Multi-class Nominal (Categories: 1 = Normal Cognition, 2 = Impaired-not-MCI, 3 = Mild Cognitive Impairment [MCI], 4 = Dementia).
- **`MOCATOTS` (MoCA Total Score):** Quantitative Interval / Discrete treated as continuous proxy (Scale: 0 to 30; values $\ge 88$ treated as special missing codes).
- **`LH_ENTORHINAL_GVOL` & `RH_ENTORHINAL_GVOL` (Entorhinal Volumes):** Quantitative Continuous, Ratio scale (Measured in $mm^3$).
- **`LH_ENTORHINAL_AVGTH` & `RH_ENTORHINAL_AVGTH` (Entorhinal Thickness):** Quantitative Continuous, Ratio scale (Measured in $mm$).
- **`NACCAGE` (Patient Age):** Quantitative Continuous, Ratio scale (Measured in years).
- **`EDUC` (Years of Education):** Quantitative Discrete, Ratio scale (Measured in years; code 99 treated as special missing).
- **`SEX` (Biological Sex):** Categorical Nominal Binary (1 = Male, 2 = Female).

## 6. Role of Variables in the Analysis
- **Primary Response Variable ($Y$):** Clinical Cognitive Status (`NACCUDSD`) for comparative classification and ANOVA models; Montreal Cognitive Assessment score (`MOCATOTS`) for linear regression models.
- **Primary Explanatory Variables ($X$):** Left and Right Entorhinal Cortical Volumes (`GVOL`) and Mean Cortical Thicknesses (`AVGTH`).
- **Covariates / Confounding Adjusters ($Z$):** Chronological Age (`NACCAGE`), Educational Attainment (`EDUC`), and Biological Sex (`SEX`).

## 7. Type of Question
Primarily **Comparative and Associative** (Evaluating group differences in cortical brain metrics across diagnostic stages, and quantifying bivariate and multivariate relationships between structural neurodegeneration and cognitive performance).

## 8. Initial Scientific Hypothesis
Progressive cognitive impairment (transition from cognitively normal status to Mild Cognitive Impairment and Alzheimer's dementia) is monotonically associated with marked volumetric atrophy and cortical thinning in temporal lobe structures (specifically the Entorhinal cortex), and this structural degradation remains statistically significant after adjusting for baseline demographic covariates (age and education).

## 9. Initial Foreseen Limitations
1. **Non-Probability Sampling / Selection Bias:** The cohort is a volunteer and clinic-referred sample with high average educational attainment ($\text{Mean} \approx 16.3$ years); it does not represent an unselected population-based probability sample.
2. **Observational Confounding & Non-Causality:** As an observational study, statistical associations cannot establish direct biological causality due to potential unmeasured genetic, cardiovascular, and lifestyle confounders.
3. **Severe Class Imbalance:** The cognitively normal group comprises approximately 68.5% of the cohort, while category 2 (`Impaired-not-MCI`) accounts for only 0.57% ($n = 7$), requiring careful consideration in downstream variance and regression diagnostics.
4. **Automated Pipeline Artifacts:** Preprocessing anomalies exist in extreme lower-bound volume measurements (e.g., near-zero volume outputs from automated segmentation in severe atrophy cases), requiring dedicated sensitivity checks in inferential phases.