import os
import pandas as pd
import numpy as np
from scipy.stats import binom

# Load and merge data
data_dir = "data"
if not os.path.exists(data_dir): data_dir = "../data"

df_mri = pd.read_csv(os.path.join(data_dir, "mriscanclean.csv"))
df_uds = pd.read_csv(os.path.join(data_dir, "udslong_imputed.csv"))
df = pd.merge(df_uds, df_mri, on="NACCID", suffixes=("_uds", "_mri"))

# Define Event: Hypertension (B)
df["Event_B"] = (df["HYPERTEN"] == 1).astype(int)

# Create Age Groups (Decades)
df["Age_Group"] = pd.cut(df["NACCAGE"], bins=[50, 60, 70, 80, 100], labels=["50-59", "60-69", "70-79", "80+"])

# Calculate global probability p
p = df["Event_B"].mean()

# Compare Observed vs Theoretical Binomial
summary = df.groupby("Age_Group")["Event_B"].agg(['count', 'sum'])
summary.columns = ['n', 'observed_k']
summary['theoretical_p'] = p
summary['expected_k'] = summary['n'] * p

print("=== PHASE 2: TASK 5 BINOMIAL APPROXIMATION ===")
print(f"Global Probability of Hypertension (p): {p:.4f}")
print("\n--- Observed vs Expected Counts (Binomial Model) ---")
print(summary.round(2))