import matplotlib.pyplot as plt
import numpy as np

verb_types = ['Type 1', 'Type 2', 'Type 4-1', 'Type 4-2']
pgt = [0.33, 0.70, 5.50, 42.3]
lst = [0.40, 0.76, 4.44, 39.1]

x = np.arange(len(verb_types))
width = 0.35

fig, ax = plt.subplots(figsize=(6, 4))
bars1 = ax.bar(x - width/2, pgt, width, label='PGT', color='#0072B2')
bars2 = ax.bar(x + width/2, lst, width, label='LST', color='#CC4049')

ax.set_ylabel('Disparity Ratio')
ax.set_xticks(x)
ax.set_xticklabels(verb_types)
ax.legend()
ax.axhline(y=1, color='black', linestyle='--', linewidth=0.8)

plt.tight_layout()
plt.savefig('disparity_ratio.pdf', bbox_inches='tight')
print("Saved!")
