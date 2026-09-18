import matplotlib.pyplot as plt
import numpy as np

verb_types = ['Type 1', 'Type 2', 'Type 4-1', 'Type 4-2']
pgt = [0.45, 0.52, 8.17, 33.2]
lst = [0.40, 0.60, 3.93, 47.4]

x = np.arange(len(verb_types))
width = 0.35

fig, ax = plt.subplots(figsize=(6, 4))
bars1 = ax.bar(x - width/2, pgt, width, label='PGT', color='#CC4049')
bars2 = ax.bar(x + width/2, lst, width, label='LST', color='#0072B2')

ax.set_ylabel('Disparity Ratio')
ax.set_xticks(x)
ax.set_xticklabels(verb_types)
ax.legend()
ax.axhline(y=1, color='black', linestyle='--', linewidth=0.8)

plt.tight_layout()
plt.savefig('disparity_ratio.pdf', bbox_inches='tight')
print("Saved!")
