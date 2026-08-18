# pygame-foundation

A foundation for building Pygame projects and games.

`pygame-foundation` is a framework built on top of Pygame that provides reusable systems for common game-development tasks. The goal is to provide useful building blocks while still keeping the flexibility of normal Pygame development.

The project is currently in active development, and additional features are planned for future releases.

**Latest version: 0.2.0**

## Documentation
[here]:https://aradpython.github.io/pygame-foundation/
You can find the documentation, [here]

---

## Installation

Install the latest version from PyPI:

```bash
pip install pygame-foundation
```

---

## Features

### Core

- `Game` class
- `World` class
- `Entity` class
- Layered rendering
- Update priorities
- Tag management
- Visibility control
- Active / paused states
- Update intervals
- Timer system

### Input

- Input Manager
- Key bindings
- Input types
- Input contexts
- Scene-specific input handling

### Camera

- Camera system
- Entity following

### Assets

- Asset Manager
- Image Assets
- Image loading and management

### Scenes

- Scene class
- Scene Manager
- Scene switching
- Scene stacking
- Scene-specific input contexts
- Covered-scene update control
- Covered-scene drawing control

### Collision

- Collision Manager
- Rectangle / AABB collision detection
- Collision groups
- Collision masks
- Two-way collision filtering
- `ENTERED` collision state
- `STAYING` collision state
- `EXITED` collision state
- Collision callbacks
- Basic AABB collision resolution

### Timers

- One-shot timers
- Repeating timers
- Limited timer loops
- Timer cancellation
- Automatic cleanup of inactive timers
- Large `dt` handling

---

## Quick Start

```python
import pygame

from pygame_foundation import Game, Entity


game = Game(
    600,
    500,
    "Pygame Foundation",
    60
)

world = game.world
input_manager = game.input_manager
camera = game.camera


player = Entity(
    x=100,
    y=100,
    size=(50, 50)
)

world.add(player)


def move_right():
    player.x += 5


input_manager.bind_key_held(
    move_right,
    pygame.K_RIGHT
)

camera.follow(player)

game.run()
```

---

## Whats New
In this release, documentation has been added. So you may refer to it via this [link][here]

---

## Project Structure

The project is organized into separate systems:

```text
pygame_foundation/
├── core/
│   ├── constants.py
│   ├── game.py
│   ├── world.py
│   ├── entity.py
│   └── timer.py
│
├── input/
│   └── manager.py
│
├── graphics/
│   └── camera.py
│
├── assets/
│   └── manager.py
│
├── scene/
│   ├── scene.py
│   └── manager.py
│
├── physics/
│   └── collision.py
│
└── utils/
    └── debug.py
```

Each system is designed to be developed independently while working together through the `Game` class.

---

## Roadmap

Planned features include:

- Controller / joystick input
- Further camera features
- Additional asset types
- Sound asset support
- Animation system
- Further physics features
- Additional collision shapes
- Performance improvements
- More game-development utilities

The roadmap may change as the framework develops and real-world projects reveal new requirements.

---

## Development

`pygame-foundation` is currently in active development.

The API may change between releases as systems are improved and new functionality is introduced.

Bug reports, suggestions, and contributions are welcome.

---

## License

This project is licensed under the MIT License.