# pygame-foundation

A foundation for building Pygame projects and games.

`pygame-foundation` is a framework built on top of Pygame that provides reusable systems for common game-development tasks. The goal is to provide useful building blocks while still keeping the flexibility of normal Pygame development.

The project is currently in active development, and additional features are planned for future releases.

**Latest version: 0.1.9**

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

## Timers

The timer system allows callbacks to be executed after a specified amount of time.

### One-shot timer

```python
game.timer_manager.after(
    1000,
    spawn_enemy
)
```

The callback will execute once after 1000 milliseconds.

### Limited loops

```python
game.timer_manager.after(
    500,
    spawn_enemy,
    loops=5
)
```

The callback will execute five times, once every 500 milliseconds.

### Repeating timer

```python
game.timer_manager.every(
    1000,
    spawn_enemy
)
```

The callback will execute every 1000 milliseconds until the timer is cancelled.

---

## Collision System

Entities can be assigned collision groups and masks to control which entities can interact with each other.

```python
player = Entity(
    x=100,
    y=100,
    size=(50, 50),
    collision_group="PLAYER",
    collision_mask={"WALL", "ENEMY", "COIN"}
)

wall = Entity(
    x=300,
    y=100,
    size=(50, 200),
    collision_group="WALL",
    collision_mask={"PLAYER"}
)
```

Collision checks can react to different collision states:

```python
from pygame_foundation.physics.collision import CollisionState


def on_collision(collision):
    print("Collision detected!")


collision_manager.add_collision_check(
    player,
    wall,
    CollisionState.ENTERED,
    on_collision
)
```

The available collision states are:

```text
ENTERED
STAYING
EXITED
```

Basic collision resolution can also be enabled:

```python
collision_manager.add_collision_check(
    player,
    wall,
    CollisionState.STAYING,
    None,
    resolve=True,
    resolve_who=player
)
```

---

## Scenes

Scenes allow different parts of a game to be separated into independent states.

For example:

```text
GameScene
    │
    ├── Player
    ├── Enemies
    └── Level

PauseScene
    │
    ├── Resume
    └── Quit
```

Scenes can also be stacked, allowing a pause menu or another overlay to appear above the current game scene.

This makes it possible to have different input contexts and behavior for different parts of a game.

---

## Camera

The camera can follow an entity:

```python
camera.follow(player)
```

This allows the game world to move relative to the screen while keeping the selected entity centered or positioned according to the camera's configuration.

---

## Assets

The Asset Manager provides centralized management of game assets.

For example:

```python
assets = game.assets

player_image = assets.load_image(
    "player",
    "assets/player.png"
)
```

Loaded assets can then be reused rather than repeatedly loading the same file.

---

## Project Structure

The project is organized into separate systems:

```text
pygame_foundation/
├── core/
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
