# 🏓 Pong Game

A simple yet classic implementation of the Pong game using Python's `turtle` module. Two players control paddles to bounce the ball back and forth, with real-time score tracking and increasing difficulty.

---

## ✅ Features

- **🎮 Two-Player Gameplay**:  
  - Left Paddle: `W` (Up), `S` (Down)  
  - Right Paddle: `↑` (Up Arrow), `↓` (Down Arrow)
- **⚡ Ball Dynamics**: Ball bounces off walls and paddles, increasing speed after each hit.
- **🧠 Scoreboard**: Displays each player’s score, updating dynamically.
- **🔁 Game Mechanics**: Ball resets when it goes out of bounds; opponent gains a point.

---

## 📁 Project Structure

```
pong-game/
├── main.py          # Game setup and loop
├── paddle.py        # Paddle class for player control
├── ball.py          # Ball class for movement and collisions
├── scoreboard.py    # Scoreboard class for score updates
```

---

## 📄 File Descriptions

- **`main.py`**: The game’s entry point. Sets up screen, players, and controls the main loop.
- **`paddle.py`**: Defines the `Paddle` class to handle movement and positioning.
- **`ball.py`**: Defines the `Ball` class for motion, bouncing, and reset logic.
- **`scoreboard.py`**: Defines the `ScoreBoard` class to display and update scores.

---

## 🕹️ How to Play

1. Clone this repository:
   ```bash
   git clone https://github.com/ehanhasainar/pong-game.git
   cd pong-game
   ```
2. Make sure Python 3 is installed.
3. Start the game:
   ```bash
   main.py
   ```

### Controls

- **Left Paddle**:  
  - `W` → Move Up  
  - `S` → Move Down  
- **Right Paddle**:  
  - `↑` → Move Up  
  - `↓` → Move Down

---

## 🖼️ Example Gameplay

- Ball starts in the center and moves in a random direction.
- Each player uses their paddle to bounce the ball back.
- Ball speed increases after each successful hit.
- When the ball passes a paddle, the opponent gains a point.
- Score is shown at the top and updates in real time.

---

## ⚙️ Customization

- **Ball Speed**: Modify `self.move_speed` in `ball.py`.
- **Paddle Size**: Adjust `stretch_wid` or `stretch_len` in `paddle.py`.
- **Screen Dimensions**: Update `screen.setup(width=800, height=600)` in `main.py`.

---

## 📦 Requirements

- Python 3.x
- The `turtle` module (comes with Python)
