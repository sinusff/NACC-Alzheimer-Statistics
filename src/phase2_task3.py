import os
import pandas as pd

# Load dataset paths
data_dir = "data"
if not os.path.exists(data_dir):
    data_dir = "../data"

# Read CSV files and merge on NACCID
df_mri = pd.read_csv(os.path.join(data_dir, "mriscanclean.csv"))
df_uds = pd.read_csv(os.path.join(data_dir, "udslong_imputed.csv"))
df = pd.merge(df_uds, df_mri, on="NACCID", suffixes=("_uds", "_mri"))

# Define Event A: Cognitive Impairment (NACCUDSD_uds >= 3)
df["Event_A"] = df["NACCUDSD_uds"] >= 3

# Define Event B: Hypertension (HYPERTEN == 1)
df["Event_B"] = df["HYPERTEN"] == 1

# Define Event C (MRI Modality): Low Left Entorhinal Volume (Below sample median)
median_vol = df["LH_ENTORHINAL_GVOL"].median()
df["Event_C_LowVol"] = df["LH_ENTORHINAL_GVOL"] < median_vol

# Baseline marginal probability P(A)
p_a = df["Event_A"].mean()

# Conditional probabilities given Hypertension (Event B)
df_b = df[df["Event_B"]]
df_not_b = df[~df["Event_B"]]
p_a_given_b = df_b["Event_A"].mean()
p_a_given_not_b = df_not_b["Event_A"].mean()

# Conditional probabilities given Low Entorhinal Volume (Event C)
df_c = df[df["Event_C_LowVol"]]
df_not_c = df[~df["Event_C_LowVol"]]
p_a_given_c = df_c["Event_A"].mean()
p_a_given_not_c = df_not_c["Event_A"].mean()

# Print structured outputs for Task 3
print("=== PHASE 2: TASK 3 CONDITIONAL PROBABILITIES ===")
print(f"Baseline Marginal P(A) [Cognitive Impairment]: {p_a:.4f} ({p_a*100:.2f}%)")

print("\n--- Condition 1: Hypertension (UDS Feature) ---")
print(f"Count with Hypertension |B|: {len(df_b)}, Impaired in B: {df_b['Event_A'].sum()}")
print(f"P(A | B)  [Impaired given Hypertension]:    {p_a_given_b:.4f} ({p_a_given_b*100:.2f}%)")
print(f"Count No Hypertension |not B|: {len(df_not_b)}, Impaired in not B: {df_not_b['Event_A'].sum()}")
print(f"P(A | ~B) [Impaired given No Hypertension]: {p_a_given_not_b:.4f} ({p_a_given_not_b*100:.2f}%)")

print("\n--- Condition 2: Low Entorhinal Volume (MRI Feature) ---")
print(f"Threshold (Sample Median of LH_ENTORHINAL_GVOL): {median_vol:.2f} mm^3")
print(f"Count with Low Volume |C|: {len(df_c)}, Impaired in C: {df_c['Event_A'].sum()}")
print(f"P(A | C)  [Impaired given Low Volume]:      {p_a_given_c:.4f} ({p_a_given_c*100:.2f}%)")
print(f"Count Normal/High Vol |not C|: {len(df_not_c)}, Impaired in not C: {df_not_c['Event_A'].sum()}")
print(f"P(A | ~C) [Impaired given Normal/High Vol]: {p_a_given_not_c:.4f} ({p_a_given_not_c*100:.2f}%)")