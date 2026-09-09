"""
analysis.py — Statistical analysis for "Not All Irregularity Is Equal"
"""

from scipy.stats import binomtest

# Dataset composition
dataset = {
    "Type 1":   2502,
    "Type 2":   1298,
    "Type 4-1": 120,
    "Type 4-2": 37,
    "Type 4-3": 1,
}
total_verbs = sum(dataset.values())  # 3958

# Error counts — unique verb method — aggregated across 5 seeds
pgt_errors = {"Type 1": 10, "Type 2": 11, "Type 4-1": 8, "Type 4-2": 19, "Type 4-3": 0}
lst_errors = {"Type 1": 13, "Type 2": 13, "Type 4-1": 7, "Type 4-2": 19, "Type 4-3": 0}

pgt_total = sum(pgt_errors.values())  # 48
lst_total = sum(lst_errors.values())  # 52

# Disparity Ratio: error share / data share
print("Disparity Ratio")
for vtype in dataset:
    data_share = dataset[vtype] / total_verbs
    dr_pgt = (pgt_errors[vtype] / pgt_total) / data_share
    dr_lst = (lst_errors[vtype] / lst_total) / data_share
    print(f"  {vtype}: PGT={dr_pgt:.2f}, LST={dr_lst:.2f}")

# Binomial test — Type 4-2 over-representation
data_share_42 = dataset["Type 4-2"] / total_verbs  # 0.00935

pgt_p = binomtest(pgt_errors["Type 4-2"], pgt_total, data_share_42, alternative="greater")
lst_p = binomtest(lst_errors["Type 4-2"], lst_total, data_share_42, alternative="greater")

print(f"\nBinomial test — Type 4-2")
print(f"  PGT: {pgt_errors['Type 4-2']}/{pgt_total}, p = {pgt_p.pvalue:.2e}")
print(f"  LST: {lst_errors['Type 4-2']}/{lst_total}, p = {lst_p.pvalue:.2e}")

# Error rate per verb type
print(f"\nError rate per verb type")
for vtype in dataset:
    pgt_rate = pgt_errors[vtype] / dataset[vtype] * 100
    lst_rate = lst_errors[vtype] / dataset[vtype] * 100
    print(f"  {vtype}: PGT={pgt_rate:.1f}%, LST={lst_rate:.1f}%")
