import os
import numpy as np
import pandas as pd

# Load dataset paths
data_dir = "data"
if not os.path.exists(data_dir):
    data_dir = "../data"

# Read CSV files and merge on NACCID
df_mri = pd.read_csv(os.path.join(data_dir, "mriscanclean.csv"))
df_uds = pd.read_csv(os.path.join(data_dir, "udslong_imputed.csv"))
df = pd.merge(df_uds, df_mri, on="NACCID", suffixes=("_uds", "_mri"))

# Define Event A: Cognitive Impairment (Disease / Target Condition)
df["Event_A"] = df["NACCUDSD_uds"] >= 3

# Define Event C: Low Left Entorhinal Volume (Test Evidence / Biomarker)
median_vol = df["LH_ENTORHINAL_GVOL"].median()
df["Event_C"] = df["LH_ENTORHINAL_GVOL"] < median_vol

total_n = len(df)

# Contingency counts
count_a = df["Event_A"].sum()
count_c = df["Event_C"].sum()
count_a_and_c = (df["Event_A"] & df["Event_C"]).sum()

# Prior probability P(A): Base rate of cognitive impairment in the cohort
p_a = count_a / total_n

# Probability of Evidence P(C): Base rate of low entorhinal volume
p_c = count_c / total_n

# Likelihood P(C | A): Sensitivity (Probability of low volume given impairment)
p_c_given_a = count_a_and_c / count_a

# Posterior probability P(A | C) using Bayes' Theorem
# P(A | C) = [ P(C | A) * P(A) ] / P(C)
p_a_given_c_bayes = (p_c_given_a * p_a) / p_c

# Direct empirical conditional probability for verification
p_a_given_c_direct = count_a_and_c / count_c

print("=== PHASE 2: TASK 9 BAYES' THEOREM PROBABILITY UPDATING ===")
print(f"Total Cohort Size (N)                 : {total_n}")
print(f"Prior Probability P(A) [Impairment]   : {p_a:.4f} ({p_a*100:.2f}%)")
print(f"Probability of Evidence P(C) [Low Vol]: {p_c:.4f} ({p_c*100:.2f}%)")
print(f"Likelihood P(C | A) [Sensitivity]     : {p_c_given_a:.4f} ({p_c_given_a*100:.2f}%)")
print(f"Posterior Probability P(A | C) [Bayes]: {p_a_given_c_bayes:.4f} ({p_a_given_c_bayes*100:.2f}%)")
print(f"Direct Empirical P(A | C)             : {p_a_given_c_direct:.4f} ({p_a_given_c_direct*100:.2f}%)")