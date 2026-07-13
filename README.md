# Computer Cricket

<p align="center">
  <a href="https://gvaishanth.github.io/Computer-Cricket/game.html"><strong>▶ Play the latest build</strong></a>
  &nbsp;•&nbsp;
  <a href="https://github.com/GVaishanth/Computer-Cricket"><strong>GitHub repository</strong></a>
</p>

<p align="center">
  A modern hand-cricket project with solo play, season mode, career progression, achievements,
  and real-time multiplayer tournaments — all built around one simple idea: pick a number, read the moment, and beat the computer or your friends.
</p>

<p align="center">
  <img src="assets/screenshots/Home%20screen.png" alt="Computer Cricket home screen" width="92%">
</p>

---

## Table of Contents
- [Live Demo](#live-demo)
- [What the project includes](#what-the-project-includes)
- [Current highlights](#current-highlights)
- [Game modes](#game-modes)
- [Screenshot gallery](#screenshot-gallery)
- [How to run](#how-to-run)
- [Project structure](#project-structure)
- [Tech stack](#tech-stack)
- [Notes and limitations](#notes-and-limitations)
- [Roadmap](#roadmap)
- [Author](#author)

---

## Live Demo

### Latest recommended build
- **Unified browser version:** [gvaishanth.github.io/Computer-Cricket/game.html](https://gvaishanth.github.io/Computer-Cricket/game.html)

### Repository
- **Source code:** [github.com/GVaishanth/Computer-Cricket](https://github.com/GVaishanth/Computer-Cricket)

### Important note
The current flagship version of the project is **`game.html`**.
It combines the solo experience (**The Nets**), multiplayer (**The League**), progression, achievements, tutorial, history, and season mode into one interface.

### Builds at a glance

| Entry point | What it contains | Status |
|---|---|---|
| `game.html` | Latest all-in-one browser build | **Recommended** |
| `computer_cricket.html` | Earlier standalone single-player web build | Legacy |
| `cricket_multiplayer.html` | Earlier standalone multiplayer web build | Legacy |
| `COMPUTER_CRICKET.py` | Original terminal version | Classic |

---

## What the project includes

### 1) The Nets — solo mode
A polished single-player hand-cricket experience against a ladder of CPU opponents, with multiple modes, toss flow, live scoreboards, innings breaks, history, and replay support.

### 2) The League — multiplayer mode
A real-time peer-to-peer tournament lobby where players can create rooms, share codes, chat, build brackets, and play live matches.

### 3) Season Mode
An IPL-style solo tournament against bots with league matches, table tracking, fixtures, playoffs, and inter-bot simulation.

### 4) Progression system
Local player profiles with XP, levels, daily tasks, weekly tasks, career stats, per-mode records, per-opponent breakdowns, and unlockable achievements.

### 5) Original CLI version
The root idea of the project in Python: a playable terminal version with the same hand-cricket number mechanics.

---

## Current highlights

### Core gameplay
- **7 game modes**: `NORMAL`, `CRAZY`, `INSANE`, `MAD`, `NOWAY`, `B10`, `TEST`
- Toss flow with bat/bowl choice
- Batting and bowling scoreboards
- Match commentary, momentum, recent-ball tracking, and live required-rate information
- Standard matches, short formats, and full **TEST** matches with multi-innings flow

### Solo experience — The Nets
- **8 CPU opponents** across difficulty tiers:
  - The Rookie
  - The Tail-ender
  - The Slogger
  - The All-Rounder
  - The Strategist
  - The Anchor
  - The Wicket Keeper
  - The Demon
- Daily challenge card on the Nets home screen
- Match history with recent results
- Rewatch support for saved matches
- Personal bests shown per mode

### Progression and profile
- Local named player profiles
- XP and level system
- Skill/profile radar view
- Daily tasks and weekly tasks
- Career stats by mode and by opponent
- **77 achievements** currently defined in the game
- Career snapshot and win/loss/tie tracking

### Season Mode
- Pick **3 to 8 bots**
- Configure matches per pair
- Choose league mode, wickets, and balls per innings
- League table, fixtures, playoffs, and season hub
- Fast-forward or watch inter-bot games

### Multiplayer — The League
- Real-time **PeerJS / WebRTC** room-based multiplayer
- Shareable **6-character room codes**
- Create room / join room flow
- Solo or team tournament formats
- Room chat, table view, and lobby controls
- Live tournament structure and host-managed flow

### Onboarding
- Interactive tutorial
- Player profile / toss-luck quiz
- In-game settings and sound controls

---

## Game modes

| Mode | Numbers | Rule summary |
|---|---|---|
| **NORMAL** | 1–10 | Same = OUT · Other = ADD |
| **CRAZY** | 1–10 | Same = ADD your number² · Adjacent = OUT · Other = ADD |
| **INSANE** | 1–10 | Same = OUT · Adjacent = MULTIPLY · Other = ADD |
| **MAD** | 1–10 | Same = ADD both numbers · Adjacent = OUT · Other = MULTIPLY |
| **NOWAY** | 1–10 | Same = MULTIPLY · Adjacent = ADD · Other = OUT |
| **B10** | 7–10 | Same = OUT · Other = ADD · 10-ball sprint |
| **TEST** | 1–6 | Same = OUT · Multi-innings match format |

---

## Screenshot gallery

### Home, onboarding, and progression

<p align="center">
  <img src="assets/screenshots/Home%20screen.png" alt="Home screen" width="48%">
  <img src="assets/screenshots/Tutorial.png" alt="Tutorial" width="48%">
</p>
<p align="center">
  <img src="assets/screenshots/Nets%20quiz.png" alt="Nets quiz" width="48%">
  <img src="assets/screenshots/Player%20profile.png" alt="Player profile" width="48%">
</p>
<p align="center">
  <img src="assets/screenshots/My%20career%20page.png" alt="My career page" width="48%">
  <img src="assets/screenshots/Achievements%20page.png" alt="Achievements page" width="48%">
</p>

### The Nets — solo mode

<p align="center">
  <img src="assets/screenshots/Nets%20home%20page.png" alt="Nets home page" width="48%">
  <img src="assets/screenshots/Toss%20page.png" alt="Toss page" width="48%">
</p>
<p align="center">
  <img src="assets/screenshots/Game%20page%20bowling.png" alt="Game page bowling" width="48%">
  <img src="assets/screenshots/game%20page%20batting.png" alt="Game page batting" width="48%">
</p>
<p align="center">
  <img src="assets/screenshots/Innings%20break.png" alt="Innings break" width="48%">
  <img src="assets/screenshots/Results%20page.png" alt="Results page" width="48%">
</p>
<p align="center">
  <img src="assets/screenshots/HIstory%20page.png" alt="History page" width="48%">
  <img src="assets/screenshots/Season%20home%20page.png" alt="Season home page" width="48%">
</p>
<p align="center">
  <img src="assets/screenshots/Season%20start%20page.png" alt="Season start page" width="70%">
</p>

### The League — multiplayer mode

<p align="center">
  <img src="assets/screenshots/Multiplayer%20home%20page.png" alt="Multiplayer home page" width="48%">
  <img src="assets/screenshots/Create%20room%20page.png" alt="Create room page" width="48%">
</p>
<p align="center">
  <img src="assets/screenshots/Join%20room%20page.png" alt="Join room page" width="48%">
  <img src="assets/screenshots/Inside%20room.png" alt="Inside room page" width="48%">
</p>

---

## How to run

### Play online
Open the latest public build here:
- [https://gvaishanth.github.io/Computer-Cricket/game.html](https://gvaishanth.github.io/Computer-Cricket/game.html)

### Run locally in a browser
Clone the repository and open `game.html`:

```bash
git clone https://github.com/GVaishanth/Computer-Cricket.git
cd Computer-Cricket
```

Then open:
- `game.html` for the latest unified version
- `computer_cricket.html` for the older standalone solo version
- `cricket_multiplayer.html` for the older standalone multiplayer version

### Run the Python version
```bash
python COMPUTER_CRICKET.py
```

---

## Project structure

```text
COMPUTER_CRICKET.py          Original Python CLI game
computer_cricket.html        Earlier standalone single-player web build
cricket_multiplayer.html     Earlier standalone multiplayer web build
game.html                    Latest unified browser version
assets/screenshots/          README screenshots
README.md                    Project documentation
```

---

## Tech stack

| Layer | Technology |
|---|---|
| Core CLI | Python 3 |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Multiplayer transport | PeerJS 1.5.4, WebRTC |
| Storage | Browser localStorage for local profiles and progress |
| Fonts | Google Fonts (`Bebas Neue`, `Rajdhani`, `Share Tech Mono`) |

---

## Notes and limitations

- **`game.html` is the current main version** and the best place to start.
- Multiplayer depends on **PeerJS/WebRTC**, so some strict networks or NAT setups may block connections.
- Progress and profiles are stored locally in the browser, so moving to another device/browser will not automatically carry data over.
- The project uses external font/CDN resources in the browser build.
- The CLI version is intentionally simple compared with the browser version.

---

## Roadmap

- Persistent cloud saves / leaderboard
- Better replay browsing and export options
- More multiplayer polish and reliability
- Additional custom modes and tournament variations
- Mobile/PWA refinements
- More profile skills, tasks, and achievement tracks

---

## Author

**G. Vaishanth**
