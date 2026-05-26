# Asteroids

A classic Asteroids arcade game built with Python and Pygame — with a Weyland-Yutani CRT aesthetic.

## Gameplay
![CRT Asteroids Visuals](IMG/asteroids_crt.mov)

## Features

- Chunky irregular asteroids that split on hit
- Phosphor-green CRT overlay with scanlines and vignette
- Score tracker styled after Alien terminal displays
- Shooting mechanic with cooldown timer

## Progress

Early prototype — basic shooting and rotation:

![Early prototype](IMG/asteroids_pt.mov)

## Project Structure
```
asteroids/
├── main.py           # Entry point and game loop
├── constants.py      # Game configuration values
├── circleshape.py    # Base class for all game objects
├── player.py         # Player ship logic
├── asteroid.py       # Asteroid logic and splitting
├── asteroidfield.py  # Asteroid spawning
├── shot.py           # Projectile logic
├── explosion.py      # Particle explosion system
├── crt.py            # CRT scanline and vignette overlay
├── logger.py         # State and event logging
└── IMG/
    ├── asteroids_crt.mov
    └── asteroids_pt.mov
```

## Requirements

- Python 3.x
- Pygame

```bash
pip install pygame
```

## Running

```bash
python main.py
```

## Controls

| Key | Action |
|-----|--------|
| `W` | Thrust forward |
| `S` | Thrust backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Shoot |
