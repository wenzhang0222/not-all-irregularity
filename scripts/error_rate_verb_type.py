import matplotlib.pyplot as plt
import numpy as np

verb_types = ['Type 1', 'Type 2', 'Type 4-1', 'Type 4-2']
pgt_error_rate = [10/2502*100, 11/1298*100,
                  8/120*100, 19/37*100]
lst_error_rate = [13/2502*100, 13/1298*100,
                  7/120*100, 19/37*100]

x = np.arange(len(verb_types))
width = 0.35

fig, ax = plt.subplots(figsize=(5, 3.5))
ax.bar([i - width/2 for i in x], pgt_error_rate,
       width, label='PGT', color='#0072B2')
ax.bar([i + width/2 for i in x], lst_error_rate,
       width, label='LST', color='#CC4049')
ax.set_ylabel('Error rate (\%)')
ax.set_xticks(x)
ax.set_xticklabels(verb_types)
ax.legend()
plt.tight_layout()
plt.savefig('error_rate.pdf', bbox_inches='tight')
print("Saved!")
