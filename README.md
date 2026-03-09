<div align="center">

# 🐢 Turtle Crossing Game

### *Cross the road. Level up. Don't get hit.*

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.x-00B140?style=for-the-badge&logo=python&logoColor=white)
![Game Dev](https://img.shields.io/badge/Game-Development-FF6B6B?style=for-the-badge)
![OOP](https://img.shields.io/badge/OOP-Based-A259FF?style=for-the-badge)

A fun, classic **arcade-style game** built with Python & Pygame where a turtle must cross a busy highway without getting hit by cars. A hands-on project to learn **Object-Oriented Programming** and **game development** concepts.

[How to Play](#-how-to-play) • [Features](#-features) • [Tech Stack](#-tech-stack) • [Getting Started](#-getting-started) • [Learning Outcomes](#-learning-outcomes)

</div>

---

## 🎮 How to Play

| Action | Control |
|--------|---------|
| Move Forward | `⬆️ Up Arrow Key` |
| Avoid Cars | Don't get hit! |
| Level Up | Reach the top edge |
| Game Over | Collide with a car |

**Objective** — Help the turtle cross the road! The game gets harder as you level up — cars move faster with every level you clear.

- 🐢 The turtle moves **forward only** when you press the `Up` key
- 🚗 Cars are **randomly generated** along the Y-axis and move right → left
- 🏁 Reaching the **top edge** sends the turtle back to start and levels up
- 💥 Colliding with a car triggers **Game Over** and stops everything

---

## ✨ Features

- 🎯 Increasing difficulty — car speed grows with each level
- 🖼️ Real image sprites using Pygame (`.png` with transparency)
- 📊 Live scoreboard showing current level
- 💥 Game Over screen on collision
- 🔄 Smooth game loop with consistent frame rate

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.10+** | Core game logic and OOP structure |
| **Pygame 2.x** | Graphics, sprites, input handling, game loop |

---

## 📁 Folder Structure

```
Turtle-Crossing-Game/
│
├── main.py              # Entry point — runs the game loop
├── player.py            # Player (turtle) class — movement & reset
├── car_manager.py       # Car spawning, movement & speed logic
├── scoreboard.py        # Level display & game over screen
│
├── images/              # Sprite assets (.png files)
│   ├── turtle.png
│   └── car.png
│
└── README.md            # You are here
```

---

## ⚙️ Getting Started

### ✅ Prerequisites

- **Python 3.10+** → [Download](https://www.python.org/downloads/)
- **pip** (comes with Python)

### 📥 1. Clone the Repository

```bash
git clone https://github.com/RuchikaaVerma/Py-Projects.git
cd Py-Projects/Turtle-Crossing-Game
```

### 📦 2. Install Dependencies

```bash
pip install pygame
```

### ▶️ 3. Run the Game

```bash
python main.py
```

---

## 🎓 Learning Outcomes

Building this game teaches key programming concepts hands-on:

**💻 Object-Oriented Programming (OOP)**
Structuring the project into classes — `Player`, `CarManager`, and `Scoreboard` — each responsible for a different part of the game.

**🔄 Game Loop**
The core structure of every game: continuously handling input → updating state → rendering graphics on every frame.

**🚧 Collision Detection**
Logic for checking if two objects (the turtle and a car) have made contact using distance-based detection.

**🖼️ Sprite Management**
Loading and manipulating `.png` image files as game objects using `convert_alpha()` for transparency support.

**📈 UI / UX Fundamentals**
Building an interactive interface with a live scoreboard and a clear Game Over screen for the player.

---

## 🔮 Roadmap

- [ ] Add sound effects on collision and level up
- [ ] High score saving between sessions
- [ ] Multiple lanes with different car speeds
- [ ] Mobile / web port using Pygame CE or Pygbag

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

Made with 🐢 and Python  
*Happy coding and happy crossing!* 🚀

</div>
