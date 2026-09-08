# 🔬 Not All Irregularity Is Equal 📝

This project presents an orthography-aware diagnosis and causal isolation of a rare failure mode in Japanese morphological inflection, showing that a single low-frequency irregular subtype accounts for a disproportionate share of neural model errors.

## License

The data is released under a Creative Commons Attribution-ShareAlike 4.0 International Public License. Please see [LICENSE.txt](https://github.com/wenzhang0222/not-all-irregularity/blob/main/LICENSE.txt) for details.

## Releasing

1. All 37 Type 4-2 verbs in our dataset with their lemma and past-tense forms in hiragana are released in [data/type42_verbs.tsv](data/type42_verbs.tsv).

2. All 19 Type 4-2 verbs that produced errors in both PGT and LST systems, confirming 100% overlap across architectures, are released in [data/type42_error_verbs.tsv](data/type42_error_verbs.tsv).
3. Figure generation scripts for all three figures in the paper are released in the [scripts/](https://github.com/wenzhang0222/not-all-irregularity/tree/main/scripts) folder:
   - [plot_disparity.py](https://github.com/wenzhang0222/not-all-irregularity/blob/main/scripts/plot_disparity.py) — Figure 1: Disparity Ratio
   - [ablation.py](https://github.com/wenzhang0222/not-all-irregularity/blob/main/scripts/ablation.py) — Figure 2: Ablation gains
   - [error_rate_verb_type.py](https://github.com/wenzhang0222/not-all-irregularity/blob/main/scripts/error_rate_verb_type.py) — Figure 3: Error rate by verb type


## Key Findings

- Type 4-2 verbs (stem-final /e/ + gemination) account for **36–40% of residual errors** despite comprising only **0.9% of the dataset**
- **Disparity Ratio**: 39–42× disproportionate error concentration
- **100% overlap**: Both PGT and LST systems fail on exactly the same 19 Type 4-2 verbs
- Removing Type 4-2 from training improves generalization more than removing all irregular verbs

## Citation

```bibtex
@inproceedings{zhang-2026-not,
    title = "Not All Irregularity Is Equal: Causally Isolating 
             a Rare Failure Mode in Japanese Morphological Inflection",
    author = "Zhang, Wen",
    booktitle = "Proceedings of the BabyLM Challenge @ EMNLP 2026",
    year = "2026"
}
```

## Link

This project was presented and published at the BabyLM Challenge @ EMNLP 2026.

The publication can be found [here](https://openreview.net/forum?id=vxEX4rQa12).

Related arXiv preprints:
- [When Irregularity Helps](https://arxiv.org/abs/2605.20558)
- [Mind Your Moras](https://arxiv.org/abs/2605.20043)

## Author

Wen Zhang — wenzhang0222@gmail.com
