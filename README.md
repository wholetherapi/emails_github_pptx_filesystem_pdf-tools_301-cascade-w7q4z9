# Cascade Retrieval

Reference implementation and experiment scripts for the paper
**Cascade Retrieval: Progressive Span Reranking for Long-Document Question Answering**
(Findings of ACL 2026).

## Repository layout

```
src/
  cascade.py          # retrieval pipeline
  index.py            # span index construction
  scoring.py          # scoring utilities
experiments/
  run_acl_suite.py    # main ACL benchmark suite
  run_ablation.py     # ablation study
results/
  acl2026_main.csv
  acl2026_ablation.csv
requirements.txt
```

## Quick start

```bash
pip install -r requirements.txt
python experiments/run_acl_suite.py --config configs/acl2026.yaml
```

The repository contains the complete released implementation together with the
experiment scripts and archived result tables used in the paper.

## Citation

```
@inproceedings{brown2026cascade,
  title={Cascade Retrieval: Progressive Span Reranking for Long-Document Question Answering},
  author={Brown, Brenda A. and Okafor, Tobias and Lindqvist, Mia},
  booktitle={Findings of ACL 2026},
  year={2026}
}
```
