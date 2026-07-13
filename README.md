# Computer Cricket

<p align="center">
  <a href="https://gvaishanth.github.io/Computer-Cricket/game.html"><strong>▶ Play the live build</strong></a>
  &nbsp;•&nbsp;
  <a href="https://github.com/GVaishanth/Computer-Cricket"><strong>Repository</strong></a>
</p>

<p align="center">
  Computer Cricket is a hand-cricket project that grew from a Python terminal game into a full browser experience with solo play, season mode, progression, achievements, and real-time multiplayer.
</p>

<p align="center">
  <img src="[https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Home%20screen.png](https://github.com/GVaishanth/Computer-Cricket/blob/main/screenshots/Home%20screen.png)" alt="Computer Cricket home screen" width="92%">
</p>

---

## Table of Contents
- [Live demo](#live-demo)
- [Repository overview](#repository-overview)
- [Current highlights](#current-highlights)
- [Game modes](#game-modes)
- [Screenshot gallery](#screenshot-gallery)
- [How to run](#how-to-run)
- [Deployment](#deployment)
- [Project structure](#project-structure)
- [Tech stack](#tech-stack)
- [Notes](#notes)
- [Roadmap](#roadmap)
- [Author](#author)

---

## Live demo

- **Latest browser build:** [gvaishanth.github.io/Computer-Cricket/game.html](https://gvaishanth.github.io/Computer-Cricket/game.html)
- **GitHub repository:** [github.com/GVaishanth/Computer-Cricket](https://github.com/GVaishanth/Computer-Cricket)

### Main entry point
The current flagship build is **`game.html`**.

It brings together:
- **The Nets** — solo mode
- **The League** — multiplayer mode
- **Season Mode**
- profile progression
- achievements
- tutorial and quiz flows
- match history and replay support

---

## Repository overview

This repository currently contains multiple versions of the project:

| File | Purpose | Status |
|---|---|---|
| `game.html` | Latest unified browser version | **Recommended** |
| `computer_cricket.html` | Older standalone single-player web version | Earlier build |
| `cricket_multiplayer.html` | Older standalone multiplayer web version | Earlier build |
| `COMPUTER_CRICKET.py` | Original Python CLI game | Classic version |
| `.github/workflows/static.yml` | GitHub Pages deployment workflow | Active |

### What the project includes

#### 1) The Nets
A solo hand-cricket experience against a ladder of CPU opponents with toss flow, multiple scoring systems, innings transitions, live scoreboards, and post-match summaries.

#### 2) The League
A real-time multiplayer room system where players can create or join a lobby, share a room code, chat, and run tournament-style matches.

#### 3) Season Mode
A solo IPL-style structure with league fixtures, tables, playoffs, and inter-bot simulations.

#### 4) Progression
Local player profiles with XP, levels, daily tasks, weekly tasks, career summaries, and achievements.

#### 5) CLI roots
The Python file preserves the original terminal version of the game and the core number-based hand-cricket concept.

---

## Current highlights

### Core gameplay
- **7 playable modes**: `NORMAL`, `CRAZY`, `INSANE`, `MAD`, `NOWAY`, `B10`, `TEST`
- Toss with bat/bowl choice
- Separate batting and bowling flow
- Live match commentary
- Required-rate and momentum indicators
- Innings transitions and result screens
- Full multi-innings support for **TEST** mode

### The Nets — solo mode
- CPU opponent ladder with **8 opponents**:
  - The Rookie
  - The Tail-ender
  - The Slogger
  - The All-Rounder
  - The Strategist
  - The Anchor
  - The Wicket Keeper
  - The Demon
- Mode selection screen with records
- Daily challenge integration
- Match history tracking
- Rewatch support
- Personal bests by mode

### Profile and progression
- Local named profiles
- XP and level system
- Career snapshot
- Radar-style player profile chart
- Daily and weekly tasks
- Career stats by mode and by opponent
- **77 achievements** currently defined in the latest build

### Season Mode
- Select **3 to 8 bots**
- Configure matches per pair
- Choose format, wickets, and balls
- League table, fixtures, and playoffs
- Fast-forward or watch inter-bot games

### The League — multiplayer
- Peer-to-peer multiplayer using **PeerJS / WebRTC**
- 6-character room codes
- Create-room and join-room flow
- Room chat and live lobby state
- Solo and tournament-style match flow

### Onboarding and polish
- Interactive tutorial
- Player quiz/profile flow
- Settings and sound controls
- Unified visual style across screens

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
| **TEST** | 1–6 | Same = OUT · multi-innings match format |

---

## Screenshot gallery

### Home, onboarding, and progression

<p align="center">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Home%20screen.png" alt="Home screen" width="48%">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Tutorial.png" alt="Tutorial" width="48%">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Nets%20quiz.png" alt="Nets quiz" width="48%">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Player%20profile.png" alt="Player profile" width="48%">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/My%20career%20page.png" alt="My career page" width="48%">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Achievements%20page.png" alt="Achievements page" width="48%">
</p>

### The Nets — solo mode

<p align="center">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Nets%20home%20page.png" alt="Nets home page" width="48%">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Toss%20page.png" alt="Toss page" width="48%">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Game%20page%20bowling.png" alt="Game page bowling" width="48%">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/game%20page%20batting.png" alt="Game page batting" width="48%">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Innings%20break.png" alt="Innings break" width="48%">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Results%20page.png" alt="Results page" width="48%">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/HIstory%20page.png" alt="History page" width="48%">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Season%20home%20page.png" alt="Season home page" width="48%">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Season%20start%20page.png" alt="Season start page" width="70%">
</p>

### The League — multiplayer mode

<p align="center">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Multiplayer%20home%20page.png" alt="Multiplayer home page" width="48%">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Create%20room%20page.png" alt="Create room page" width="48%">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Join%20room%20page.png" alt="Join room page" width="48%">
  <img src="https://raw.githubusercontent.com/GVaishanth/Computer-Cricket/main/assets/screenshots/Inside%20room.png" alt="Inside room" width="48%">
</p>

---

## How to run

### Browser
Clone the repo and open the HTML file you want:

```bash
git clone https://github.com/GVaishanth/Computer-Cricket.git
cd Computer-Cricket
```

Then open one of these in your browser:
- `game.html` → latest unified version
- `computer_cricket.html` → earlier solo-only build
- `cricket_multiplayer.html` → earlier multiplayer-only build

### Python CLI
```bash
python COMPUTER_CRICKET.py
```

---

## Deployment

This repository already includes a GitHub Pages workflow:

- **Workflow file:** `.github/workflows/static.yml`
- On push to `main`, GitHub Pages deploys the repository as static content.

Current live page:
- [https://gvaishanth.github.io/Computer-Cricket/game.html](https://gvaishanth.github.io/Computer-Cricket/game.html)

---

## Project structure

```text
.github/workflows/static.yml  GitHub Pages deployment
COMPUTER_CRICKET.py           Original Python CLI version
computer_cricket.html         Earlier standalone single-player build
cricket_multiplayer.html      Earlier standalone multiplayer build
game.html                     Latest unified browser build
assets/screenshots/           README screenshots
README.md                     Project documentation
```

---

## Tech stack

| Layer | Technology |
|---|---|
| CLI | Python 3 |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Multiplayer | PeerJS 1.5.4, WebRTC |
| Storage | Browser localStorage |
| Fonts | Bebas Neue, Rajdhani, Share Tech Mono |

---

## Notes

- **`game.html` is the main version** of the project.
- The older HTML files are still useful as separate milestone builds.
- Multiplayer depends on PeerJS/WebRTC, so some networks may block connections.
- Progress is stored locally in the browser.
- For the screenshots in this README to display on GitHub, the files inside `assets/screenshots/` must exist in the `main` branch.

---

## Roadmap

- Persistent cloud saves or leaderboard support
- More replay and match archive features
- Better multiplayer reliability and polish
- Extra tournament and custom-mode options
- More progression tasks and achievement tracks
- PWA/mobile refinement

---

## Author

**G. Vaishanth**
