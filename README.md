# TFE26-093: Improving Imperfect-Information Reasoning in Ludii through Constraint-Based Hypothesis Generation

### Previously known as *Improving General Game AI for Modern Board Games*

**Author(s):** LECHAT Jérôme (50351800 - jerome.lechat@student.uclouvain.be) \
**Supervisor(s):** PIETTE Éric \
**Reader(s):** DUHOUX Benoît, MORENVILLE Achille, VERHAEGHE Hélène \
**Year:** 2025-2026

## Structure of this repository

```bash
TFE26-093/
├── Thesis/
│ ├── ...
│ ├── dissertation.pdf   # The final version of this Master Thesis
│ └── ...
├── TAG/                 # Git Submodules N°1
│ ├── BENCHMARKS
│     ├── figs           # The different plots
│     ├── logs           # The logs output from the CECI clusters run
│     ├── results        # The officiel outputs of the Benchmark
│     ├── scripts        # The SCRUM scripts made for the CECI clusters
│     ├── ...            # (Python Scripts)
│     └── setupANDrun.sh # The script to setup the venv and plotting
│ └── src
│     └── main
│         └── java
│             └── games
│                 ├── battleship_basic   # The random determinization
│                 ├── battleship_best    # The heatmap guided det.
│                 └── battleship_smart   # The constraint-based det.
├── Ludii/               # Git Submodules N°2
│ ├── BENCHMARKS
│     ├── figs           # The different plots
│     ├── logs           # The logs output from the CECI clusters run
│     ├── results        # The officiel outputs of the Benchmark
│     ├── scripts        # The SCRUM scripts made for the CECI clusters
│     ├── ...            # (Python scripts)
│     └── setupANDrun.sh # The script to setup the venv and plotting
│ ├── base_r1.nft
│ └── AI
│     └── src
│         └── utils
│             ├── BattleshipBenchmark.java   # The Tournament System
│             ├── BattleshipDeterminizationAgent.java   # The OSLA-like (port from TAG)
│             ├── ContextDeterminizer.java   # Handles determinization
│             ├── DeterminizationEngine.java   # Port of TAG's Constraint-Based Determinization we made
│             └── DeterminizedAgent.java   # The Generic Wrapper
└── README.md            # You are here!
```

---

## ⚠️ Important: Git Submodules Required

This repository relies on Git submodules (such as the `TAG/`  or `Ludii/` directory). A standard `git clone` will only download empty placeholder folders. To clone the entire project along with its dependencies, please use the appropriate commands below.

### 1. If you haven't cloned the repository yet
Include the `--recursive` flag to fetch everything at once:
```bash
git clone --recursive <REPOSITORY_URL>
