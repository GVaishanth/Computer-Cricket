# Computer Cricket

An interactive cricket simulation available in three forms — a Python CLI game, a single-player web app, and a real-time multiplayer tournament platform — all built around the same hand-cricket number mechanics.

---

## Overview

Computer Cricket is a number-based cricket game where players compete by selecting numbers each ball. The game simulates real cricket concepts: toss, innings, scoring, wickets, and match outcomes using custom rule sets across seven distinct game modes.

The project covers **game logic design**, **user interaction**, **modular programming**, and **real-time peer-to-peer networking**.

---

## Files

| File | Description |
|---|---|
| `COMPUTER_CRICKET.py` | Original Python CLI game |
| `computer_cricket.html` | Single-player web version with themes and UI |
| `cricket_multiplayer.html` | Real-time multiplayer tournament platform |

---

## Game Modes

All three versions share the same seven modes:

| Mode | Numbers | Rule |
|---|---|---|
| **NORMAL** | 1–10 | Same = OUT · Other = ADD |
| **CRAZY** | 1–10 | Same = ADD your number² · Adjacent = OUT · Other = ADD |
| **INSANE** | 1–10 | Same = OUT · Adjacent = MULTIPLY (you × cpu) · Other = ADD |
| **MAD** | 1–10 | Same = ADD (you + cpu) · Adjacent = OUT · Other = MULTIPLY |
| **NOWAY** | 1–10 | Same = MULTIPLY · Adjacent = ADD · Other = OUT |
| **B10** | 7–10 | Same = OUT · Other = ADD · 10 balls only |
| **TEST** | 1–6 | Same = OUT · 2 innings per side · Follow-on at 150-run deficit |

---

## Python CLI — `COMPUTER_CRICKET.py`

### Features
- Toss system with Heads/Tails call and Bat/Bowl decision
- All 7 game modes fully implemented
- **TEST mode** — 2 innings per side, follow-on rule, win by an innings
- **B10 mode** — 10-ball match, restricted number pool (7–10)
- Player type detection quiz (Batsman / Bowler / All-rounder) that influences toss outcomes
- Input validation — out-of-range numbers clamped, non-numeric input replaced with random
- Tie-breaker system using a randomly selected mode
- Post-game menu: Continue, Change Mode, Random, Quit
- Mode banners showing rules at the start of each game
- 25 functions, ~625 lines

### How to Run
```bash
python COMPUTER_CRICKET.py
```

### How to Play
1. Complete the optional player type quiz (or skip)
2. Choose a game mode: `NORMAL | CRAZY | INSANE | MAD | NOWAY | B10 | TEST`
3. Win the toss and choose to Bat or Bowl
4. Enter numbers each ball — rules vary by mode
5. Defend or chase the target in the second innings

---

## Single-Player Web — `computer_cricket.html`

A fully featured browser game. No install required — just open in any browser.

### Features
- All 7 game modes with correct rules
- **National team colour themes** — each mode switches the entire UI to its team's 3-colour palette:
  - Home/Lobby → Afghanistan (Navy · Red · Blue)
  - NORMAL → New Zealand (Black · White · Silver)
  - CRAZY → Australia (Green · Gold · Navy)
  - INSANE → India (Navy · Saffron · Green)
  - MAD → West Indies (Maroon · Gold · Dark Red)
  - NOWAY → England (Navy · Red · White)
  - B10 → South Africa (Green · Gold · Red)
  - TEST → Classic Whites (Cream · Navy · Sepia)
- **Luck quiz** — 10-round number quiz determines player type, influences toss outcomes
- **Difficulty system** — Easy (CPU avoids your number) / Normal / Hard (CPU targets your number)
- **Between-innings summary card** — shows scores, target, and who bats next before continuing
- **Live stats row** — run rate, runs needed per ball, innings number
- **Last 6 balls log** — coloured dot row showing each ball outcome
- **Ball-by-ball commentary** — mode-specific flavour text for every outcome type
- **Session stats** — wins, losses, ties, high score, personal best per mode, win streak
- **Match history** — last 30 matches with mode, difficulty, scores, margin
- **Per-mode personal best** displayed on mode select cards
- **TEST mode** — full 4-innings match, follow-on at 150-run deficit, win by an innings
- **Keyboard input** — 1–9 and 0 for 10
- Back-to-menu button on all screens
- 52 JS functions, 57 KB

---

## Multiplayer — `cricket_multiplayer.html`

A real-time tournament platform. No server, no account — just share a 6-character room code.

### Network
Uses **PeerJS** (WebRTC) via the free public `0.peerjs.com` signalling server. Works cross-device over the internet. The host is the single source of truth; all state is broadcast to every connected player.

### Room Setup (Host)
- Room size: 2–12 players
- Wickets per innings (1–10)
- Balls per innings (0 = unlimited)
- Timer per ball: 3–15 seconds (host configures)
- Match type: Solo (1v1) or Team (2 teams)
- Gameplay mode: Single (fixed), Double (2 modes random per match), Random (any mode)

### Tournament Format — IPL Style
- **League stage** — every player/team plays every other twice
- **Points table** — 2 pts per win, NRR as tiebreaker
- **Knockouts** — top 4 advance: Qualifier 1 (1v2), Eliminator (3v4), Qualifier 2, Final
- Host can launch the next match from lobby or result screen

### Match Flow
1. **Match entry screen** — matched players choose to Enter Match or Forfeit (walkover win)
2. **Toss** — coin flip with call; loser's outcome influenced by player type from luck quiz
3. **Bat/Bowl choice** — toss winner decides
4. **Playing** — configurable countdown timer per ball; both players lock numbers simultaneously
5. **Reveal** — both numbers shown for 1 second before next ball
6. **Unpicked = 0** — if a player doesn't lock before timer, their number defaults to 0
7. **Innings break** — 3.5-second break with target info before second innings
8. **Result** — winner, scores, margin, mode played; host sees Next Match button

### TEST Mode (Multiplayer)
- 4 innings total — each side bats twice
- Normal order: A bats → B bats → A bats → B chases
- Follow-on enforced automatically at 150-run deficit
- Win by an innings checked after follow-on innings
- Live innings tracker shows all 4 innings with running totals

### Team Match
- Computer randomly selects 2 captains
- Captains alternate picking players (live draft)
- Captain selects bowler before each over
- Bowler over limit enforced (total overs ÷ bowlers × 2)

### Spectating
- All non-playing players watch live
- Locked numbers shown as ✓ until both players lock, then revealed simultaneously
- Reaction buttons: 🎉 YAY!! · 👎 BOO!! · 😮 NOOO!! · 🏏 HOWZAT! · 6️⃣ SIX! · 🔥 ON FIRE! · 🦆 DUCK!
- Reactions float up on screen for all viewers

### Lobby & Stats
- Scrolling live ticker — current match, upcoming matches, last result
- Lobby chat (all players) + Team chat (private per team)
- Standings table — wins, losses, points, NRR
- Tournament bracket — league + knockouts with live/done/upcoming status
- Continue tournament option after final

### Responsive Layout
- **Mobile** — stacked: match → upcoming → ticker → chat → stats
- **Desktop** — 3-column: upcoming+standings | match | chat+bowling figures
- Team colour themes applied to entire UI during each match

### 91 JS functions, 99 KB

---

## Technologies Used

| Layer | Technology |
|---|---|
| CLI game | Python 3 — `random`, `time` |
| Web UI | HTML5 · CSS3 (custom properties, grid, animations) |
| Web logic | Vanilla JavaScript (ES6+) |
| Real-time networking | PeerJS 1.5.4 (WebRTC) |
| Fonts | Google Fonts — Bebas Neue, Rajdhani, Share Tech Mono |

---

## Deployment — GitHub Pages

1. Create a GitHub repository
2. Upload `computer_cricket.html` and `cricket_multiplayer.html` to the root
3. Go to **Settings → Pages → Branch: main → Save**
4. Access at:
   - `https://yourusername.github.io/reponame/computer_cricket.html`
   - `https://yourusername.github.io/reponame/cricket_multiplayer.html`

No build step. No dependencies to install. No server needed.

---

## Project Structure

```
COMPUTER_CRICKET.py          # Python CLI game (625 lines, 25 functions)
computer_cricket.html        # Single-player web app (57 KB, 52 functions)
cricket_multiplayer.html     # Multiplayer tournament (99 KB, 91 functions)
README.md                    # This file
```

---

## Limitations

- Multiplayer relies on PeerJS cloud signalling — may fail behind symmetric NAT (some corporate/school networks)
- No persistent data — stats reset on page refresh (single-player) or when host closes tab (multiplayer)
- CLI version is terminal-only with no GUI
- Team mode requires at least 4 players for a meaningful draft

---

## Future Enhancements

- Persistent leaderboard using localStorage or a lightweight backend
- Sound effects and haptic feedback on mobile
- TURN server support for 100% NAT traversal in multiplayer
- Replay system — save and watch ball-by-ball match replays
- Custom game modes — user-defined rules
- Mobile app wrapper (PWA)

---

## Author

**G. Vaishanth**
