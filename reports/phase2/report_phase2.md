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

  ---

## Task 5: Discrete and Binomial Distributions

In this task, we evaluate the applicability of the Binomial distribution to model the occurrence of Hypertension (Event $B$) within our cohort ($N = 1,237$). A Binomial model $B(n, p)$ is predicated on three key assumptions:
1. A fixed number of trials ($n$).
2. A constant probability of success ($p$).
3. Independence of trials.

### 1. Model Definition
* **Success Event ($B$):** Participant has a history of Hypertension (`HYPERTEN` = 1).
* **Global Probability ($p$):** Calculated from the total sample as $P(B) = \frac{444}{1237} \approx 0.3589$.
* **Trials ($n$):** Subsets grouped by age decades.

### 2. Empirical Validation
The following table compares the observed number of hypertensive cases ($k$) in each age group with the theoretical counts expected under the Binomial model ($n \times p$):

| Age Group | Sample Size ($n$) | Observed Cases ($k$) | Expected Cases ($n \times p$) |
| :--- | :---: | :---: | :---: |
| 50–59 | 172 | 41 | 61.74 |
| 60–69 | 556 | 189 | 199.57 |
| 70–79 | 414 | 182 | 148.60 |
| 80+ | 69 | 31 | 24.77 |

### 3. Model Approximation Assessment
* **Violation of Binomial Assumptions:** The data fails to conform to the Binomial model.
* **Key Findings:**
    1. **Non-Constant Probability:** The Binomial model requires a fixed $p$. However, the observed cases ($k$) show a clear age-dependent trend. In the 50–59 group, the model overestimates hypertension risk (41 observed vs. 61.7 expected), while in the 70–79 and 80+ groups, it underestimates the observed cases.
    2. **Age-Dependency:** Since the prevalence of hypertension is biologically linked to aging, the probability of "success" ($p$) is not constant across age trials, violating the Binomial assumption of fixed probability.
* **Conclusion:** The Binomial distribution is not a suitable model for this clinical event. Future modeling should utilize more flexible frameworks, such as Logistic Regression, to account for the age-dependent nature of hypertension prevalence.

---

## Task 6: Continuous Variables and Normal Distribution Assessment

In this task, we rigorously examine whether the empirical distribution of our primary continuous neuroimaging biomarker—**Left Entorhinal Cortical Thickness** (`LH_ENTORHINAL_AVGTH`, measured in millimeters)—can be adequately approximated by a Gaussian (Normal) distribution. 

Evaluating normality is essential because downstream parametric procedures in Phase 3 (e.g., two-sample $t$-tests and ANOVA) and Phase 4 (Ordinary Least Squares regression) rely on distributional assumptions regarding continuous variables and their error terms.

### 1. Empirical Summary and Distributional Moments
Based on the complete multimodal cohort ($N = 1,237$):

| Metric | Sample Value | Theoretical Normal Standard | Interpretation |
| :--- | :---: | :---: | :--- |
| **Sample Size ($N$)** | $1,237$ | — | High statistical power |
| **Sample Mean ($\mu$)** | $2.9698\text{ mm}$ | — | Center of mass |
| **Sample Median** | $3.0210\text{ mm}$ | $\mu$ | High central agreement ($\Delta = 0.05\text{ mm}$) |
| **Standard Deviation ($\sigma$)** | $0.3841\text{ mm}$ | — | Moderate dispersion |
| **Sample Skewness** | $-0.7333$ | $0.0000$ | Moderate negative (left) skewness |
| **Excess Kurtosis** | $1.3396$ | $0.0000$ | Moderate leptokurtic profile (peakedness) |

### 2. Empirical Rule Evaluation ($68\% - 95\% - 99.7\%$)
We evaluate the proportion of sample observations falling within integer standard deviation intervals around the empirical mean:

* **Within $\mu \pm 1\sigma$ $[2.5857, 3.3539]\text{ mm}$:** Observed **$71.54\%$** (Theoretical: $68.27\%$)
* **Within $\mu \pm 2\sigma$ $[2.2016, 3.7380]\text{ mm}$:** Observed **$95.39\%$** (Theoretical: $95.45\%$)
* **Within $\mu \pm 3\sigma$ $[1.8175, 4.1221]\text{ mm}$:** Observed **$99.19\%$** (Theoretical: $99.73\%$)

The empirical coverage within $\pm 2\sigma$ exhibits near-perfect agreement ($95.39\%$ vs. $95.45\%$) with classical Gaussian theory, demonstrating that the vast majority of participants adhere closely to normal dispersion characteristics.

### 3. Visual Diagnostics (Figure 6)
Visual inspection via `figures/fig6_normality_check.png` confirms two structural properties:
1. **Histogram with Fitted Normal Density (Left Panel):** The empirical density demonstrates a bell-shaped contour centered near $3.0\text{ mm}$. The modal frequency slightly exceeds the theoretical Gaussian peak, corroborating the positive excess kurtosis ($1.34$).
2. **Normal Quantile-Quantile (Q-Q) Plot (Right Panel):** For the bulk of the cohort (theoretical quantiles between $-1.5$ and $+2.0$), empirical quantiles follow the red reference diagonal line linearly. However, pronounced downward departure is evident in the extreme lower tail (theoretical quantiles $< -2.0$), indicating a heavier left tail than expected under strict Gaussianity.

### 4. Formal Statistical Tests and Sample Size Sensitivity
* **Shapiro-Wilk Test:** $W = 0.9726, \quad p = 1.5024 \times 10^{-14}$
* **D'Agostino-Pearson $K^2$ Test:** $K^2 = 128.0746, \quad p = 1.5451 \times 10^{-28}$

**Critical Discussion on Normality Rejection:**  
Both formal tests strictly reject the null hypothesis of normality ($p < 0.05$). However, as emphasized in modern statistical pedagogy, formal goodness-of-fit tests are notoriously hypersensitive in large samples ($N = 1,237$); they detect trivial, practically negligible departures from Gaussianity that do not invalidate parametric modeling. 

### 5. Biological Rationale for Left-Tail Asymmetry
The observed left skewness ($-0.7333$) and downward Q-Q plot departure are biologically expected in a clinical memory cohort. Cognitively normal older adults cluster around a physiological cortical thickness plateau ($\approx 3.0\text{ to } 3.4\text{ mm}$). Conversely, progressive neurodegenerative pathology in Mild Cognitive Impairment (`MCI`) and Alzheimer's Dementia produces pathological cortical thinning (atrophy), dragging a prolonged tail down toward $1.5 - 2.0\text{ mm}$ (and down to $0.88\text{ mm}$ in extreme segmentation artifacts).

### 6. Methodological Decision for Subsequent Phases
* **Applicability:** While strict mathematical normality is rejected due to pathology-induced left-tail skewness, the **Normal approximation remains practically serviceable** for central parametric inference. 
* **Justification:** By virtue of the Central Limit Theorem ($N = 1,237 \gg 30$), sample estimators of the mean will possess asymptotically normal sampling distributions.
* **Mitigation:** In Phase 3 and Phase 4, parametric linear models will be complemented with non-parametric sensitivity checks and robust standard errors to protect inference against the heavy lower tail.

---

## Task 7: Expected Value and Variance

In probability and descriptive statistics, the **Expected Value** ($E[X]$ or sample mean $\mu$) measures the central tendency or long-run average of a quantitative random variable, while the **Variance** ($Var(X)$ or sample variance $s^2$) quantifies the dispersion, spread, or uncertainty of the observations around that center. 

Using our complete multimodal Alzheimer's cohort ($N = 1,237$), we compute the empirical expected value and variance for key demographic, clinical, and neuroimaging variables.

### 1. Summary of Empirical Mean and Variance (Exact Data)

| Variable Description | Code | Sample Mean ($E[X]$) | Sample Variance ($s^2$) | Standard Deviation ($s$) |
| :--- | :--- | :---: | :---: | :---: |
| **Participant Age** | `NACCAGE` | $68.19\text{ years}$ | $64.63\text{ yrs}^2$ | $8.04\text{ years}$ |
| **MoCA Cognitive Score** | `MOCATOTS` | $24.44\text{ points}$ | $20.14\text{ pts}^2$ | $4.49\text{ points}$ |
| **Left Entorhinal Thickness** | `LH_ENTORHINAL_AVGTH` | $2.97\text{ mm}$ | $0.1476\text{ mm}^2$ | $0.38\text{ mm}$ |
| **Right Entorhinal Thickness** | `RH_ENTORHINAL_AVGTH` | $3.06\text{ mm}$ | $0.1610\text{ mm}^2$ | $0.40\text{ mm}$ |

### 2. Substantive Interpretation in the Context of the Study

* **Participant Age (`NACCAGE`):** 
  - *Expected Value ($68.19$ years):* Represents the empirical average age of individuals evaluated at memory clinics within this cohort, confirming a typical older adult sample targeted for neurodegenerative assessments.
  - *Variance ($64.63\text{ yrs}^2$, Std $\approx 8.04$):* Reflects a wide chronological age spread (ranging from $41$ to $91$ years), providing sufficient demographic variance to control for age as a confounding covariate in downstream regression models.

* **Cognitive Function (`MOCATOTS`):** 
  - *Expected Value ($24.44$ points):* Denotes the overall average cognitive performance of the cohort. Because a score of $\ge 26$ is typically considered normal, a mean of $24.44$ reflects the mixed clinical spectrum of the sample, which includes both healthy controls and cognitively impaired patients (`MCI` and Dementia).
  - *Variance ($20.14\text{ pts}^2$, Std $\approx 4.49$):* Captures the cognitive heterogeneity across diagnostic subgroups, demonstrating a broad distribution of performance levels.

* **Structural Brain Biomarkers (`LH/RH_ENTORHINAL_AVGTH`):** 
  - *Expected Value ($2.97\text{ mm}$ left, $3.06\text{ mm}$ right):* Indicates the baseline structural cortical thickness in the medial temporal lobe, showing strong bilateral symmetry across the sample.
  - *Variance ($0.1476\text{ mm}^2$ left, $0.1610\text{ mm}^2$ right):* Quantifies the combined inter-individual anatomical differences and disease-driven cortical thinning (atrophy) characteristic of progressive cognitive decline.

### 3. Methodological Significance
These exact empirical expectations and variances establish the foundational distributional parameters required for standardized scoring ($Z$-scores), confidence interval estimation in Phase 3, and residual error variance evaluations in Phase 4.

---

## Task 8: Bivariate Random Variables, Scatter Plots, and Covariance

To investigate the joint behavior of clinical cognition and neurostructural integrity, we analyze two continuous random variables: **Global Cognitive Performance** (`MOCATOTS`, $Y$) and **Left Entorhinal Cortical Thickness** (`LH_ENTORHINAL_AVGTH`, $X$). 

Evaluating these variables simultaneously allows us to quantify their linear association through empirical covariance, correlation coefficients, and bivariate graphical visualization (`Figure 8`).

### 1. Empirical Covariance and Correlation Metrics
Based on our complete matched cohort ($N = 1,233$ complete pairs after sanitization):
* **Sample Covariance ($Cov(X, Y)$):** $\approx 0.4863$ ($\text{mm} \cdot \text{points}$)
* **Pearson Correlation Coefficient ($r$):** $\approx 0.2825$ ($p < 0.001$)
* **Spearman Rank Correlation ($\rho$):** $\approx 0.2786$

### 2. Graphical Analysis via Scatter Plot (`Figure 8`)
The bivariate scatter plot (`figures/fig8_bivariate_scatter.png`) maps left entorhinal cortical thickness against MoCA total scores, stratified by clinical diagnostic status:
* **Trend and Direction:** The dashed black linear regression trendline slopes upward from left to right, confirming a positive direction of association between cortical thickness and cognitive performance.
* **Diagnostic Clustering:** 
  - **Normal Cognition (`Normal`, red points):** Heavily concentrated in the upper-right region, demonstrating preserved cortical thickness ($> 2.5\text{ mm}$) and high cognitive scores ($\ge 25$).
  - **Alzheimer's Dementia (`Dementia`, green points):** Dispersed toward the lower-left region, reflecting significant structural atrophy alongside severe cognitive deficits.
  - **Mild Cognitive Impairment (`MCI`, blue points):** Form an intermediate transitional layer between healthy participants and dementia cases.

### 3. Statistical Interpretation
* **Positive Association:** The positive sample covariance ($0.4863$) and correlation ($r = 0.2825$) establish that greater cortical thickness is associated with higher cognitive test scores within this clinical referral cohort.
* **Effect Size:** A Pearson $r$ of $0.2825$ represents a weak-to-moderate linear relationship. While medial temporal atrophy is a fundamental biomarker of Alzheimer's disease, global cognitive performance is also modulated by educational attainment, cognitive reserve, and widespread neural networks outside the entorhinal cortex.

### 4. Methodological Caveats
* **Non-Causality:** As established in our observational study design, correlation does not prove causation. Unmeasured confounders (such as age, education, and vascular health) simultaneously impact brain morphometry and cognition.
* **Forward Application:** This bivariate foundation provides the empirical justification for multivariable linear regression modeling in Phase 4, where confounding variables will be explicitly controlled.

---

## Task 9: Bayes' Theorem and Probability Updating

In clinical diagnosis and statistical modeling, **Bayes' Theorem** provides a rigorous mathematical framework for updating our degree of belief (or probability) regarding a patient's condition as new empirical evidence becomes available. 

Using our multimodal dataset ($N = 1,237$), we apply Bayes' Theorem to update the probability of cognitive impairment (Event $A$) given structural neuroimaging evidence (Event $C$: Low Left Entorhinal Volume).

### 1. Definition of Events and Parameters
* **Event $A$ (Target Condition / Disease):** Cognitive Impairment (`NACCUDSD_uds` $\ge 3$, encompassing `MCI` and Dementia).
* **Event $C$ (Test Evidence / Biomarker):** Low Left Entorhinal Volume (`LH_ENTORHINAL_GVOL` below the sample median of $1545.00\text{ mm}^3$).

From our empirical data, we extract the baseline parameters required for Bayesian updating:
* **Prior Probability $P(A)$:** The baseline marginal probability of cognitive impairment in the cohort:
  $$P(A) = \frac{383}{1,237} \approx 0.3096 \quad (30.96\%)$$
* **Probability of Evidence $P(C)$:** The marginal probability of observing low entorhinal volume across the sample:
  $$P(C) = \frac{618}{1,237} \approx 0.4996 \quad (49.96\%)$$
* **Likelihood / Sensitivity $P(C \mid A)$:** The probability of observing low entorhinal volume given that the individual is cognitively impaired:
  $$P(C \mid A) = \frac{|A \cap C|}{\text{Count}(A)} = \frac{225}{383} \approx 0.5875 \quad (58.75\%)$$

### 2. Application of Bayes' Theorem
We compute the **Posterior Probability** $P(A \mid C)$—the updated probability of cognitive impairment given the presence of low entorhinal volume—using Bayes' formula:
$$P(A \mid C) = \frac{P(C \mid A) \cdot P(A)}{P(C)}$$

Substituting the empirical values:
$$P(A \mid C) = \frac{0.5875 \times 0.3096}{0.4996} \approx \frac{0.1819}{0.4996} \approx 0.3641 \quad (36.41\%)$$

*(Note: This direct empirical conditional probability $P(A \cap C) / P(C) = 225 / 618 \approx 0.3641$ confirms the exact mathematical consistency of the Bayesian update).*

### 3. Statistical and Clinical Interpretation
* **Probability Revision:** Observing structural neuroimaging evidence (low entorhinal volume) updates our prior belief of cognitive impairment from a baseline of **$30.96\%$** to a posterior risk of **$36.41\%$**.
* **Clinical Utility:** The application of Bayes' theorem demonstrates quantitatively how multimodal data integration (`UDS + MRI`) refines clinical assessment. Structural neurobiology acts as a probabilistic updater, confirming that localized brain atrophy elevates the diagnostic probability of cognitive decline within a specialized memory clinic setting.

