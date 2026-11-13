# Data Directory: NACC Alzheimer's Multimodal Subcohort

## 1. Official Data Provenance
- **Originating Repository:** National Alzheimer's Coordinating Center (`NACC`)
- **Supervising Agency:** National Institute on Aging (`NIA`), National Institutes of Health (`NIH`)
- **Collection Mechanism:** Standardized clinical evaluations across $>30$ Alzheimer's Disease Research Centers (`ADRCs`) in the United States.
- **Protocol Epoch:** Uniform Data Set (`UDS`) protocol (initiated September 2005 onwards).
- **Date Received / Initialized:** Fall 1405 (Academic Session).

---

## 2. Required Data Files (Locally Maintained)
In compliance with project security guidelines, raw data files are excluded from version control via `.gitignore`:
1. `mriscanclean.csv` (851 KB): Structural volumetric ($mm^3$) and thickness ($mm$) MRI features parcellated using the `FreeSurfer` pipeline.
2. `udslong_imputed.csv` (905 KB): Curated clinical and neuropsychological assessments, pre-imputed by dataset curators.
3. `combined_adjacency_matrix.csv`: 62-by-62 structural cortical connectivity matrix.

---

## 3. Data Flow and Processing Pipeline
1. **Multimodal Alignment:** Both modalities share the unique subject key `NACCID`. Merging both files yields exactly $1,237$ common participants with $0$ unmatched records.
2. **Independence Rule:** Each row corresponds to a single, cross-sectionally matched index visit coinciding with the MRI scan date, satisfying the $i.i.d.$ observation assumption.
3. **Special Missing Codes Sanitization:**
   - `MOCATOTS`: Values $\ge 88$ (indicating missing/unassessed tests) are mapped to `NaN`.
   - `EDUC`: Value $99$ (unknown education code) is mapped to `NaN`.
4. **Diagnostic Harmonization (`NACCUDSD`):** Numeric codes are mapped to clinical labels:
   - `1.0` $\rightarrow$ `Normal Cognition` ($n = 847$, $68.47\%$)
   - `2.0` $\rightarrow$ `Impaired (Not MCI)` ($n = 7$, $0.57\%$)
   - `3.0` $\rightarrow$ `Mild Cognitive Impairment [MCI]` ($n = 252$, $20.37\%$)
   - `4.0` $\rightarrow$ `Dementia` ($n = 131$, $10.59\%$)