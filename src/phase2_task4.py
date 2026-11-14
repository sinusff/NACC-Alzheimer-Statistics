import os
import pandas as pd

# Load dataset paths
data_dir = "data"
if not os.path.exists(data_dir):
    data_dir = "../data"

# Read and merge
df_mri = pd.read_csv(os.path.join(data_dir, "mriscanclean.csv"))
df_uds = pd.read_csv(os.path.join(data_dir, "udslong_imputed.csv"))
df = pd.merge(df_uds, df_mri, on="NACCID", suffixes=("_uds", "_mri"))

# Event A: Cognitive Impairment
p_a = (df["NACCUDSD_uds"] >= 3).mean()

# Event B: Hypertension
p_b = (df["HYPERTEN"] == 1).mean()

# Joint Probability P(A and B)
p_a_and_b = ((df["NACCUDSD_uds"] >= 3) & (df["HYPERTEN"] == 1)).mean()

# Independence check: P(A) * P(B)
p_a_times_p_b = p_a * p_b

print("=== PHASE 2: TASK 4 INDEPENDENCE EVALUATION ===")
print(f"Empirical Joint Probability P(A ∩ B) : {p_a_and_b:.4f}")
print(f"Product of Marginals P(A) * P(B)      : {p_a_times_p_b:.4f}")
print(f"Absolute Difference                   : {abs(p_a_and_b - p_a_times_p_b):.4f}")

# Comparison logic for the report
if abs(p_a_and_b - p_a_times_p_b) < 0.01:
    print("\nStatus: Data appears consistent with the assumption of independence.")
else:
    print("\nStatus: Data suggests statistical dependence (P(A∩B) != P(A)*P(B)).")