# Computer Cricket (CLI Game)

An interactive command-line cricket simulation built in Python, featuring multiple game modes, dynamic gameplay mechanics, and adaptive AI behavior.

---

## Overview

Computer Cricket is a number-based cricket game where players compete against the computer by selecting numbers. The game simulates real cricket concepts such as toss, innings, scoring, and match outcomes using logical rules and randomness.

The project focuses on **game logic design**, **user interaction**, and **modular programming**.

---

## Features

### Core Gameplay
- Toss system (Bat / Bowl decision)
- Batting and bowling simulation
- Real-time score tracking
- Win/Loss/Tie conditions

### Multiple Game Modes
- **NORMAL** – Standard gameplay (same number = out)
- **CRAZY** – Same number = square, adjacent = out
- **INSANE** – Adjacent = multiply, same = out
- **MAD** – Mixed scoring rules
- **NOWAY** – Reverse logic gameplay
- **B10** – 10-ball fast match with restricted numbers

### Smart Mechanics
- Randomized AI opponent
- Input validation and fallback handling
- Tie-breaker system with random mode selection

### Additional Systems
- Player type detection (Batsman / Bowler / All-rounder)
- Dynamic rule variations across modes
- Modular function-based structure

---

## Technologies Used

- **Language:** Python
- **Concepts:**
  - Conditional Logic
  - Game Design
  - Randomization
  - Modular Programming

---

## How to Run

bash
```python COMPUTER_CRICKET.py```

## 🎮 How to Play

1. Choose a game mode:
   NORMAL | CRAZY | INSANE | MAD | NOWAY | B10

2. Toss determines batting or bowling

3. Enter numbers (1–10):
- Same number → OUT (varies by mode)
- Different numbers → runs scored

4. Defend or chase the target

---

## ⚠️ Rules Summary

- Numbers outside range are adjusted automatically
- Invalid input → replaced with random number
- Tie → random tie-breaker mode

---

## 📁 Project Structure

COMPUTER_CRICKET.py # Main game file

---

## ⚠️ Limitations

- CLI-based interface (no GUI)
- No persistent score tracking
- Heavy reliance on user input

---

## 🚀 Future Enhancements

- 🧪 **Test Match Mode (Planned)**
  - Multi-innings gameplay
  - Extended number set (1–6)
  - Strategic long-format gameplay

- GUI version (Tkinter / Web)
- Difficulty levels for AI
- Scoreboard and match history
- Multiplayer support

---

## 👤 Author

**G. Vaishanth**
