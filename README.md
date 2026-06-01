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
│ └── AI
│     └── src
│         └── utils
│             ├── BattleshipBenchmark.java   # The Tournament System
│             ├── BattleshipDeterminizationAgent.java   # The OSLA-like (port from TAG)
│             ├── ContextDeterminizer.java   # Handles determinization
│             ├── DeterminizationEngine.java   # Port of TAG's Constraint-Based Determinization we made
│             └── DeterminizedAgent.java   # The Generic Wrapper
├── Lechat_50351800_2026.pdf   # The final PDF
├── README.md                  # You are here!
└── run_hallucinator.py        # The Open-Source tool used by the faculty
```

---

## ⚠️ Important: Git Submodules Required

This repository relies on Git submodules (such as the `TAG/`  or `Ludii/` directory). A standard `git clone` will only download empty placeholder folders. To clone the entire project along with its dependencies, please use the appropriate commands below.

### 1. If you haven't cloned the repository yet
Include the `--recursive` flag to fetch everything at once:
```bash
git clone --recursive <REPOSITORY_URL>
```

---

## ⚠️ Note on Hallucinator Validation

First, do not forget to init a venv and install the correct dependencies

```bash
# Creating venv
python3 -m venv venv

# Activating the venv
source venv/bin/activate

# Installing dependencies
pip install --quiet --upgrade pip
pip install hallucinator

# Then run the .py at the root of this repo
python run_hallucinator.py
```

The bibliography (`dissertation.bib`) has been pre-screened using the faculty's `hallucinator` validation tool.

Please note that the tool's strict reliance on DOIs and academic databases generates expected `[not_found]` false positives for several valid primary sources. This includes ludological references (historical board games, rulebooks, patents) and specific non-indexed preprints provided by the supervisory team. All flagged sources are intentional and have been manually verified.

Here are the results, and their correction that I made myself

```bash
(venv) gg@miniGOLIATH:~/Documents/TFE26-093$ /home/gg/Documents/TFE26-093/venv/bin/python /home/gg/Documents/TFE26-093/run_hallucinator.py
1. Lecture du fichier dissertation.bib...
Entry type patent not standard. Not considered.
2. 40 références structurées avec succès.
3. Initialisation du validateur...
4. Requêtes de validation en cours (cela peut prendre quelques secondes par papier)...

--- RÉSULTATS OFFICIELS ---
[verified] Artificial Intelligence and Games
[verified] Kasparov versus Deep Blue: Computer Chess Comes of Age
[verified] CHINOOK: The World Man-Machine Checkers Champion
[verified] Mastering the game of Go with deep neural networks and tree search
[verified] Kriegsspiel
[verified] Stratego
[not_found] Battleship
[not_found] TAG: A Tabletop Games Framework   # Available here https://gaigresearch.github.io/projects/TAG
[verified] Ludii - The Ludemic General Game System
[not_found] Ludii Language Reference   # Available here https://ludii.games/downloads/LudiiLanguageReference.pdf
[verified] The Ludii Games Database: A Resource for Computational and Cultural Research on Traditional Board Games
[verified] Ludii as a Competition Platform
[not_found] General Game Playing: Overview of the AAAI Competition   # Available here https://dl.acm.org/doi/10.1609/aimag.v26i2.1813
[not_found] General Game Playing: Game Description Language Specification   # Available here http://ggp.stanford.edu/readings/gdl_spec.pdf
[not_found] A survey of Monte Carlo tree search methods   # Available here https://ieeexplore.ieee.org/document/6145622
[mismatch] Rolling horizon evolutionary algorithms for general video game playing
[not_found] Information set Monte Carlo tree search   # Available here https://ieeexplore.ieee.org/document/6203567
[verified] Optimised Playout Implementations for the Ludii General Game System
[not_found] Ludii Game Logic Guide   # Available here https://ludii.games/downloads/LudiiGameLogicGuide.pdf
[verified] CADIA PLAYER: A simulation-based general game player
[verified] Constraint-Based Symmetry Detection in General Game Playing
[verified] WoodStock : un programme-joueur générique dirigé par les contraintes stochastiques
[not_found] Artificial Intelligence: A Modern Approach   # Available here https://aima.cs.berkeley.edu/
[not_found] Planning and acting in partially observable stochastic domains   # Available here https://www.sciencedirect.com/science/article/pii/S000437029800023X
[not_found] Heads-up limit hold’em poker is solved   # Available here https://dl.acm.org/doi/10.1145/3131284
[not_found] Valet: A Standardized Testbed of Traditional Imperfect-Information Card Games   # Available here https://arxiv.org/abs/2603.03252
[not_found] Report on the 2nd Digital Ludeme Project Workshop   # Available here https://journals.sagepub.com/doi/10.3233/ICG-220211
[not_found] GameTable COST Action: kickoff report   # Available here https://journals.sagepub.com/doi/10.3233/ICG-240245
[verified] Ludii General Game System for Modeling, Analyzing, and Designing Board Games
[verified] General Board Game Concepts
[verified] Game AI for Cultural Heritage: Outcomes from the GameTable 3rd Grant Period Opening Meeting
[verified] GAVEL: Generating Games Via Evolution and Language Models
[verified] An Empirical Evaluation of Two General Game Systems: Ludii and RBG
[verified] Bandit based Monte-Carlo planning
[verified] Progressive strategies for Monte-Carlo tree search
[not_found] Design and Implementation of TAG: A Tabletop Games Framework   # Available here https://arxiv.org/abs/2009.12065
[verified] A course in game theory
[verified] Modeling Uncertainty: Constraint-Based Belief States in Imperfect-Information Games
[verified] Belief Stochastic Game: A Model for Imperfect-Information Games with Known Positions
[verified] Understanding the Success of Perfect Information
Monte Carlo Sampling in Game Tree Search
```
