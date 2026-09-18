# 🔬 Not All Irregularity Is Equal 📝

This project presents an orthography-aware diagnosis and causal isolation of a rare failure mode in Japanese morphological inflection, showing that a single low-frequency irregular subtype accounts for a disproportionate share of neural model errors.

## License

The data is released under a Creative Commons Attribution-ShareAlike 4.0 International Public License. Please see [LICENSE.txt](https://github.com/wenzhang0222/not-all-irregularity/blob/main/LICENSE.txt) for details.

## Releasing

1. All 37 Type 4-2 verbs in our dataset with their lemma and past-tense forms in hiragana are released in [data/type42_verbs.tsv](https://github.com/wenzhang0222/not-all-irregularity/blob/main/data/type42_verbs.tsv).

2. Figure generation scripts for all three figures in the paper are released in the [scripts/](https://github.com/wenzhang0222/not-all-irregularity/tree/main/scripts) folder:
   * [error_rate_verb_type.py](https://github.com/wenzhang0222/not-all-irregularity/blob/main/scripts/error_rate_verb_type.py) — Figure 1: Error rate by verb type
   * [plot_disparity.py](https://github.com/wenzhang0222/not-all-irregularity/blob/main/scripts/plot_disparity.py) — Figure 2: Disparity Ratio
   * [ablation.py](https://github.com/wenzhang0222/not-all-irregularity/blob/main/scripts/ablation.py) — Figure 3: Ablation gains

3. The statistical analysis script (Disparity Ratio + binomial test) is released in [scripts/analysis.py](https://github.com/wenzhang0222/not-all-irregularity/blob/main/scripts/analysis.py).

4. Numerical results for all experiments are released in the 
[results/](https://github.com/wenzhang0222/not-all-irregularity/tree/main/results) folder:
   * [ablation_results.tsv](https://github.com/wenzhang0222/not-all-irregularity/blob/main/results/ablation_results.tsv) — accuracy under all 8 ablation conditions
   * [error_distribution.tsv](https://github.com/wenzhang0222/not-all-irregularity/blob/main/results/error_distribution.tsv) — error distribution by verb type
   * [disparity_ratios.tsv](https://github.com/wenzhang0222/not-all-irregularity/blob/main/results/disparity_ratios.tsv) — Disparity Ratio values
   * [error_rates.tsv](https://github.com/wenzhang0222/not-all-irregularity/blob/main/results/error_rates.tsv) — error rate per verb type

## Key Findings

- Type 4-2 verbs (stem-final /e/ + gemination) account for **30–43% of residual errors** despite comprising only **0.9% of the dataset**
- **Disparity Ratio**: 34–48× disproportionate error concentration
- Removing Type 4-2 from training improves generalization more than removing all irregular verbs

## Citation

If you use this data or code, please cite:

```bibtex
@inproceedings{zhang-2026-not,
    title = "Not All Irregularity Is Equal: Causally Isolating 
             a Rare Failure Mode in Japanese Morphological Inflection",
    author = "Zhang, Wen",
    booktitle = "Proceedings of the BabyLM Challenge @ EMNLP 2026",
    year = "2026",
    note = "To appear"
}
```

## Link

This project has been accepted at the BabyLM Challenge @ EMNLP 2026.

Related arXiv preprints:
- [When Irregularity Helps](https://arxiv.org/abs/2605.20558)
- [Mind Your Moras](https://arxiv.org/abs/2605.20043)

## Author

Wen Zhang — wenzhang0222@gmail.com
