import os
import pandas as pd

# Load dataset paths dynamically
data_dir = "data"
if not os.path.exists(data_dir):
    data_dir = "../data"

# Read CSV files and merge on NACCID
df_mri = pd.read_csv(os.path.join(data_dir, "mriscanclean.csv"))
df_uds = pd.read_csv(os.path.join(data_dir, "udslong_imputed.csv"))
df = pd.merge(df_uds, df_mri, on="NACCID", suffixes=("_uds", "_mri"))

# 1. Define UDS Event (U): Clinical Cognitive Impairment (MCI or Dementia)
df["Event_U_Impaired"] = df["NACCUDSD_uds"] >= 3

# 2. Define Constructed MRI Event (M): Bilateral Entorhinal Cortical Thinning
# Defined as cortical thickness below the sample median in BOTH left and right hemispheres
med_lh_th = df["LH_ENTORHINAL_AVGTH"].median()
med_rh_th = df["RH_ENTORHINAL_AVGTH"].median()
df["Event_M_BilateralThinning"] = (
    (df["LH_ENTORHINAL_AVGTH"] < med_lh_th) &
    (df["RH_ENTORHINAL_AVGTH"] < med_rh_th)
)

total_n = len(df)

# Contingency table with margins
ct = pd.crosstab(
    df["Event_U_Impaired"],
    df["Event_M_BilateralThinning"],
    margins=True,
    margins_name="Total",
)

# Extract exact counts
n_u = df["Event_U_Impaired"].sum()
n_m = df["Event_M_BilateralThinning"].sum()
n_u_and_m = (df["Event_U_Impaired"] & df["Event_M_BilateralThinning"]).sum()
n_u_and_not_m = (df["Event_U_Impaired"] & (~df["Event_M_BilateralThinning"])).sum()
n_not_m = (~df["Event_M_BilateralThinning"]).sum()
n_not_u = (~df["Event_U_Impaired"]).sum()
n_not_u_and_m = ((~df["Event_U_Impaired"]) & df["Event_M_BilateralThinning"]).sum()

# Marginal Probabilities
p_u = n_u / total_n
p_m = n_m / total_n

# Joint Probability P(U and M)
p_u_and_m = n_u_and_m / total_n

# Conditional Probabilities (both directions)
p_u_given_m = n_u_and_m / n_m
p_u_given_not_m = n_u_and_not_m / n_not_m
p_m_given_u = n_u_and_m / n_u
p_m_given_not_u = n_not_u_and_m / n_not_u

print("=== PHASE 2: PATH C - C.3 MULTIMODAL JOINT PROBABILITY ===")
print(f"Thresholds -> Left Median: {med_lh_th:.4f} mm | Right Median: {med_rh_th:.4f} mm")
print(f"Total Sample Size (N): {total_n}\n")

print("--- Contingency Table (U: Impaired vs. M: Bilateral Thinning) ---")
print(ct)

print("\n--- Marginal Probabilities ---")
print(f"P(U) [Cognitive Impairment]          : {p_u:.4f} ({p_u*100:.2f}%)")
print(f"P(M) [Bilateral Entorhinal Thinning] : {p_m:.4f} ({p_m*100:.2f}%)")

print("\n--- Joint Probability ---")
print(f"P(U and M) [Joint Occurrence]        : {p_u_and_m:.4f} ({p_u_and_m*100:.2f}%)")
print(f"Product P(U) * P(M) [If Independent] : {p_u * p_m:.4f}")

print("\n--- Conditional Probabilities ---")
print(f"P(U | M)  [Impaired given Thinning]     : {p_u_given_m:.4f} ({p_u_given_m*100:.2f}%)")
print(f"P(U | ~M) [Impaired given No Thinning]  : {p_u_given_not_m:.4f} ({p_u_given_not_m*100:.2f}%)")
print(f"P(M | U)  [Thinning given Impaired]     : {p_m_given_u:.4f} ({p_m_given_u*100:.2f}%)")
print(f"P(M | ~U) [Thinning given Not Impaired] : {p_m_given_not_u:.4f} ({p_m_given_not_u*100:.2f}%)")