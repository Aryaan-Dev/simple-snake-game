# 🐍 Snake Game

*Dive into a classic Snake game with a twist! Eat the food, grow longer, and beat your highscore of 130. Move with arrow keys, avoid crashing, and enjoy the fun beats. Ready to slither to the top? Let’s go! 🎮*

## ✨ Cool Features

- Grow by eating red food!
- Track your score and highscore.
- Fun background music and sound effects.
- Simple, addictive gameplay.

## 🌟 How to Play Snake Game

Get this game running on your PC with these easy steps:

1. **Clone the Repository**\
   Grab the code:

   ```bash
   git clone https://github.com/Aryaan-Dev/Snake-Game.git
   cd Snake-Game
   ```

2. **Set Up Your Environment**

   - Make sure Python 3.6+ is installed.

3. **Install Dependencies**\
   Install the needed package:

   ```bash
   pip install pygame
   ```

4. **Prepare Audio Files**

   - Place `start.mp3`, `background.mp3`, and `gameover.mp3` in the project folder.
   - Ensure `highscore.txt` is present (default highscore is 130).

5. **Run the Game**\
   Start it with:

   ```bash
   python game1.py
   ```

   - Press SPACE to start, use arrow keys to move, and ENTER to replay after game over.

**Tip**: Keep your sound on for the full experience!

## 🛠️ Troubleshooting

Having trouble? Check these fixes:

### 1. **Game Doesn’t Start**

- **Signs**: Error like “ModuleNotFoundError” or no window.
- **Fix**: Install pygame with `pip install pygame`. Check Python version with `python --version` (needs 3.6+).

### 2. **No Sound Plays**

- **Signs**: Silent game despite audio files.
- **Fix**: Verify `start.mp3`, `background.mp3`, and `gameover.mp3` are in the folder. Check file names match the script.

### 3. **Game Crashes or Freezes**

- **Signs**: Window closes or stops responding.
- **Fix**: Ensure no other app uses the same audio device. Update pygame or restart your PC.

### 4. **Highscore Not Saving**

- **Signs**: Highscore resets to 0.
- **Fix**: Check write permissions for `highscore.txt`. Run as administrator if needed.

### 5. **Black Screen**

- **Signs**: Window opens but stays black.
- **Fix**: Confirm `game1.py` and audio files are in the folder. Check terminal for errors.

**Still Stuck?** Share your issue on GitHub with the error message!

## 📋 Requirements

- **Python 3.6+**: The game engine.
- **Dependencies**: `pygame` (install via `pip install pygame`).
- **Files**: `start.mp3`, `background.mp3`, `gameover.mp3`, `highscore.txt`.

## 💻 Virtual Environment Tips

Keep it tidy with a virtual env:

- **Create**: `python -m venv venv`
- **Activate**:
  - Windows: `venv\Scripts\activate`
  - Mac/Linux: `source venv/bin/activate`
- **Install**: `pip install pygame`
- **Deactivate**: `deactivate`

## 👨‍💻 Made By

Created with passion by B P ARYAAN \[ Aryaan-Dev \].

## 🤝 Join the Fun

Love it? Fork it, improve it, or report bugs on GitHub!

---

**Built with ❤️ for little gamers !**
