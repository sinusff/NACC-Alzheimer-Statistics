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

# Define Event B: Presence of Hypertension (HYPERTEN == 1)
df["Event_B"] = df["HYPERTEN"] == 1

# Total sample size
total_n = len(df)

# Contingency Table (Cross-tabulation of Event A and Event B)
contingency_table = pd.crosstab(
    df["Event_A"], df["Event_B"], margins=True, margins_name="Total"
)

# Joint count and Joint Probability P(A and B)
joint_count = df[df["Event_A"] & df["Event_B"]].shape[0]
joint_prob = joint_count / total_n

# Print results for Task 2 validation
print("=== PHASE 2: TASK 2 CONTINGENCY TABLE (Cross-tabulation) ===")
print(contingency_table)
print(f"\nJoint Count |A and B|: {joint_count}")
print(
    f"Joint Probability P(A and B): {joint_prob:.4f} ({joint_prob * 100:.2f}%)"
)