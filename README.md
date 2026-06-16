# Pokemon-GUI-Battler

A fully interactive, 2-player Pokémon battling game built in Python using `tkinter` for the graphical user interface and `pandas` for data management. Choose your Pokémon, utilize elemental advantages, and evolve your champions in a race to win 3 rounds!

## 🌟 Features

*   **Interactive GUI:** Built entirely with Python's built-in `tkinter` library, featuring health bars, score tracking, and click-based combat.
*   **Turn-Based Combat:** Players take turns choosing between physical attacks and elemental attacks.
*   **Elemental Type Advantages:** Built-in strengths and weaknesses (e.g., Water beats Fire, Fire beats Grass). Using an elemental attack with a type advantage has an 80% chance to land a Critical Hit!
*   **Evolution Mechanics:** When a player loses a round, the winning player's Pokémon evolves into its next form, gaining updated stats for the next battle.
*   **Data Driven:** Reads raw Pokémon stats from a CSV file and filters the dataset dynamically using `pandas`.
