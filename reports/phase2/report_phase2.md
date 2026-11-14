# Phase 2 Report: Probability and Probabilistic Distributions
## NACC Multimodal Alzheimer's Dataset Analysis

---

## Phase 2 Overview
In this phase, the real-world multimodal clinical (`UDS`) and neuroimaging (`MRI`) data of 1,237 participants from the `NACC` database are translated into the formal language of **probability and probabilistic distributions**. The core objective is to model uncertainty, analyze the independence or dependency of clinical events (such as cognitive decline and vascular conditions), define quantitative random variables, and study discrete and continuous distributions to build a solid foundation for statistical inference in subsequent phases.

---

## Task 1: Definition of Events and Random Variables

To analyze the probabilistic structure of the dataset, the sample space ($S$) is defined as the entire independent cohort of this study, comprising **1,237 patients** ($N = 1,237$). Based on this, clinical random events and quantitative random variables are operationally formulated as follows:

### 1. Sample Space ($S$)
The set of all 1,237 independent participants (`Independent Participants`) present in the integrated `NACC` database who possess complete clinical and neuroimaging profiles:
$$S = \{ \omega_1, \omega_2, \dots, \omega_{1,237} \}$$

### 2. Event $A$ (Cognitive Impairment)
* **Conceptual Definition:** The event of randomly selecting a patient from the sample cohort who exhibits moderate-to-severe cognitive impairment (diagnosed with Mild Cognitive Impairment `MCI` or Dementia).
* **Operational Definition:** The diagnostic variable `NACCUDSD_uds` takes the value of `3.0` (Mild Cognitive Impairment) or `4.0` (Dementia).
* **Empirical Calculation:** Out of 1,237 individuals, 383 patients satisfied this condition; thus, the empirical probability of this event is:
  $$P(A) = \frac{383}{1,237} \approx 0.3096 \quad (30.96\%)$$

### 3. Event $B$ (Hypertension)
* **Conceptual Definition:** The event of randomly selecting a patient from the sample cohort who has a documented medical history of high blood pressure (`Hypertension`).
* **Operational Definition:** The medical variable `HYPERTEN` equals `1.0`.
* **Empirical Calculation:** 444 patients presented with a history of hypertension; thus, the empirical probability of this event is:
  $$P(B) = \frac{444}{1,237} \approx 0.3589 \quad (35.89\%)$$

### 4. Random Variable $X$ (Cognitive Score)
* **Conceptual Definition:** A quantitative function mapping each randomly selected patient from the sample space to their Montreal Cognitive Assessment score (`MoCA Total Score`).
* **Operational Definition:** The quantitative variable `MOCATOTS` with a theoretical domain ranging from 0 to 30.
* **Empirical Distribution Summary of Random Variable $X$:**
  - Empirical Mean ($\mu_X$): $24.44$
  - Standard Deviation ($\sigma_X$): $4.49$
  - Median: $25.40$
  - Range (`Min - Max`): $[0.0, 39.4]$ (reflecting extreme baseline anomalies audited in Phase 1).

  ---

## Task 2: Marginal and Joint Probabilities

To investigate the co-occurrence of clinical cognitive impairment and vascular risk factors within our cohort ($N = 1,237$), we analyze the marginal and joint empirical probabilities of Event $A$ (Cognitive Impairment, where `NACCUDSD_uds` $\ge 3$) and Event $B$ (Hypertension, where `HYPERTEN` $= 1$).

### 1. Contingency Table (Cross-Tabulation)
The empirical joint frequency distribution between cognitive diagnostic status and hypertension is summarized in the contingency table below:

| Events | Hypertension ($B$) | No Hypertension ($\overline{B}$) | Marginal Total ($A$ / $\overline{A}$) |
| :--- | :---: | :---: | :---: |
| **Cognitive Impairment ($A$)** | $148$ | $235$ | **$383$** |
| **Normal Cognition ($\overline{A}$)** | $296$ | $558$ | **$854$** |
| **Marginal Total ($B$ / $\overline{B}$)** | **$444$** | **$793$** | **$1,237$** |

### 2. Marginal Probabilities
From Task 1 and the marginal totals above, the individual empirical probabilities for each event are:
- **Marginal Probability of Event $A$ ($P(A)$):** The empirical probability that a randomly chosen patient in the cohort suffers from cognitive impairment (`MCI` or Dementia):
  $$P(A) = \frac{383}{1,237} \approx 0.3096 \quad (30.96\%)$$
- **Marginal Probability of Event $B$ ($P(B)$):** The empirical probability that a randomly chosen patient has a documented history of hypertension:
  $$P(B) = \frac{444}{1,237} \approx 0.3589 \quad (35.89\%)$$

### 3. Joint Probability $P(A \cap B)$
The joint probability represents the empirical likelihood that a randomly selected individual from the sample suffers from **both** cognitive impairment *and* hypertension simultaneously:
$$P(A \cap B) = \frac{|A \cap B|}{\text{Total } N} = \frac{148}{1,237} \approx 0.1196 \quad (11.96\%)$$

### 4. Statistical Interpretation
- **Dual Burden:** The empirical joint probability indicates that approximately $11.96\%$ of the entire memory clinic cohort ($148$ out of $1,237$ patients) present with the combined comorbidity of cognitive decline (`MCI` or Dementia) and high blood pressure.
- **Foundation for Independence Testing:** These exact marginal and joint frequencies provide the mathematical framework required for subsequent evaluations of statistical independence or conditional probability between vascular health and neurological status in the following tasks.

  ---
  
## Task 3: Conditional Probability Analysis

In this task, we evaluate the dependencies between clinical/neuroimaging features and cognitive status by calculating **conditional probabilities**. Specifically, we assess how the likelihood of cognitive impairment ($A$) changes when conditioned on vascular health (Event $B$: Hypertension) or structural brain integrity (Event $C$: Low Left Entorhinal Volume).

### 1. Defining Conditional Events
- **Event $A$:** Cognitive Impairment (`NACCUDSD_uds` $\ge 3$).
- **Event $B$:** Presence of Hypertension (`HYPERTEN` $= 1$).
- **Event $C$:** Low Left Entorhinal Volume (`LH_ENTORHINAL_GVOL` $<$ Sample Median).

### 2. Analysis of Clinical Feature ($B$)
We calculate the probability of cognitive impairment given the presence versus the absence of hypertension.

* **Conditional Probability $P(A|B)$:**
  $$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{148}{444} \approx 0.3333 \quad (33.33\%)$$

* **Conditional Probability $P(A|\overline{B})$:**
  $$P(A|\overline{B}) = \frac{P(A \cap \overline{B})}{P(\overline{B})} = \frac{235}{793} \approx 0.2963 \quad (29.63\%)$$

**Interpretation:** The presence of hypertension increases the empirical probability of cognitive impairment from the baseline of $30.96\%$ to $33.33\%$. This suggests a positive conditional association between vascular risk factors and cognitive impairment within this cohort.

### 3. Analysis of Neuroimaging Biomarker ($C$)
We define Event $C$ as having an entorhinal volume below the sample median ($1545.00 \text{ mm}^3$).

* **Conditional Probability $P(A|C)$:**
  $$P(A|C) = \frac{P(A \cap C)}{P(C)} = \frac{225}{618} \approx 0.3641 \quad (36.41\%)$$

* **Conditional Probability $P(A|\overline{C})$:**
  $$P(A|\overline{C}) = \frac{P(A \cap \overline{C})}{P(\overline{C})} = \frac{158}{619} \approx 0.2553 \quad (25.53\%)$$

**Interpretation:** Conditioning on structural MRI evidence reveals a more substantial shift in risk. Patients with low entorhinal volume exhibit a notably higher risk of impairment ($36.41\%$) compared to those with preserved volume ($25.53\%$). The conditional risk difference observed for the MRI biomarker ($\approx 10.88\%$) is significantly larger than that of the vascular factor ($\approx 3.70\%$), suggesting a stronger predictive relationship between entorhinal atrophy and cognitive decline in this dataset.

### 4. Concluding Remarks
The analysis demonstrates that both hypertension and neurostructural atrophy update our prior knowledge regarding cognitive status. However, the magnitude of the probability update provided by the structural MRI marker is more pronounced. These empirical findings provide a strong quantitative basis for multivariate modeling in subsequent phases.

  ---

## Task 4: Evaluating the Concept of Independence

In this task, we assess the independence of two clinical events: Event $A$ (Cognitive Impairment, defined as `NACCUDSD_uds` $\ge 3$) and Event $B$ (Presence of Hypertension, defined as `HYPERTEN` $= 1$). 

Two events $A$ and $B$ are statistically independent if and only if the joint probability of their occurrence equals the product of their marginal probabilities:
$$P(A \cap B) = P(A) \times P(B)$$

### 1. Empirical Calculation
Based on the full cohort of $N = 1,237$ participants:

* **Marginal Probability $P(A)$:** $0.3096$
* **Marginal Probability $P(B)$:** $0.3589$
* **Product of Marginals $P(A) \times P(B)$:** $0.3096 \times 0.3589 \approx 0.1111$
* **Empirical Joint Probability $P(A \cap B)$:** $0.1196$

### 2. Independence Evaluation
To evaluate independence, we compute the absolute difference between the empirical joint probability and the product of marginals:
$$\Delta = |P(A \cap B) - (P(A) \times P(B))|$$
$$\Delta = |0.1196 - 0.1111| = 0.0085$$

### 3. Statistical Interpretation
The observed absolute difference of approximately $0.0085$ ($< 1\%$) suggests that the empirical distribution of these data is consistent with the assumption of statistical independence. In this specific cohort, the presence of hypertension does not show a strong empirical deviation from what would be expected under the independence assumption regarding cognitive impairment status.

**Methodological Note:** While these events appear independent based on simple empirical probability, this analysis is restricted to the bivariate level. Potential conditional dependencies or multivariate interactions between vascular risk factors, neuroimaging biomarkers, and cognitive status will be more rigorously examined in the inferential modeling phases.
