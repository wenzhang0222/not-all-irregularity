import matplotlib.pyplot as plt
import numpy as np

conditions = ['-4', '-4-1', '-4-2', '-4-3',
              '-4-1,4-2', '-4-1,4-3', '-4-2,4-3']
pgt_gains = [0.97, 0.98, 1.00, 0.76, 0.97, 0.72, 0.49]
lst_gains = [1.22, 0.45, 2.02, 1.01, 2.01, 0.71, 1.00]

x = np.arange(len(conditions))
width = 0.35

fig, ax = plt.subplots(figsize=(7, 3.5))
bars1 = ax.bar(x - width/2, pgt_gains, width,
               label='PGT', color='#0072B2')
bars2 = ax.bar(x + width/2, lst_gains, width,
               label='LST', color='#CC4049')
ax.set_ylabel('Accuracy gain (\%)')
ax.set_xticks(x)
ax.set_xticklabels(conditions, rotation=30, ha='right')
ax.legend()
ax.axhline(y=0, color='black', linewidth=0.5)
plt.tight_layout()
plt.savefig('ablation_gains.pdf', bbox_inches='tight')
print("Saved!")
