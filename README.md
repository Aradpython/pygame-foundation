# pygame-foundation

A foundation for building Pygame projects and games.

`pygame-foundation` is a framework built on top of Pygame that provides reusable systems for common game-development tasks, allowing you to focus more on building your game instead of repeatedly implementing the same underlying systems.

The project is currently in active development, and additional features are planned for future releases.

**Latest version: 0.1.8**

## Installation

```bash
pip install pygame-foundation
```
or 
```bash
python -m pip install pygame-foundation
```

## Features

### Core

- Game class
- World class
- Entity class
- Layered rendering
- Update priorities
- Tag management
- Visibility control
- Active/paused states
- Update intervals

### Input

- Input Manager
- Input Bindings
- Input Types
- Input Contexts
- Scene-specific input contexts

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

### Physics

- Collision Manager
- Rectangle/AABB collision detection
- Collision groups
- Collision masks
- `ENTERED`, `STAYING`, and `EXITED` collision states
- Collision callbacks
- Basic collision resolution

## Quick Start

```python
import pygame

from pygame_foundation import Game, Entity, World


game = Game(600, 500, "Pygame Foundation", 60)

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

## Collision Example

Collision checks can be registered between entities and can optionally execute callbacks when a specific collision state occurs.

```python
from pygame_foundation.physics.collision import CollisionState


def on_coin_collected(collision):
    print("Coin collected!")


collision_manager.add_collision_check(
    player,
    coin,
    CollisionState.ENTERED,
    on_coin_collected
)
```

Collision checks support three main states:

```text
ENTERED
STAYING
EXITED
```

Collision filtering can also be used to control which entities are allowed to collide.

```python
player = Entity(
    100,
    100,
    size=(50, 50),
    collision_group="PLAYER",
    collision_mask={"WALL", "ENEMY", "COIN"}
)

wall = Entity(
    300,
    100,
    size=(50, 200),
    collision_group="WALL",
    collision_mask={"PLAYER"}
)
```

Basic collision resolution can be enabled when an entity should not remain overlapping another entity.

```python
collision_manager.add_collision_check(
    player,
    wall,
    CollisionState.ENTERED,
    None,
    resolve=True,
    resolve_who=player
)
```

## Project Structure

```text
pygame_foundation/
├── core/
├── input/
├── camera/
├── assets/
├── scene/
├── physics/
└── utils/
```

The framework is organized into separate systems so that individual features can be developed and expanded independently.

## Roadmap

Planned features include:

- Controller / joystick input
- Further camera features
- Further asset types
- Sound asset support
- Animation system
- Timer system
- Additional physics features
- More collision shapes
- Performance improvements

## Development

`pygame-foundation` is actively developed, and APIs may change between releases as the framework evolves.

Feedback, bug reports, and contributions are welcome.

## License

This project is licensed under the MIT License.