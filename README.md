# pygame-foundation

A foundation for building Pygame projects and games.

`pygame-foundation` is currently in active development, with additional features planned for future versions.

The latest version is **v0.1.6**. This release introduces asset-loading functionality through the new Asset Manager and Image Asset systems, along with bug fixes and improvements.

## Installation

```bash
pip install pygame-foundation
```

## Features

- Game class
- World class
- Entity class
- Layered rendering
- Update priorities
- Tag management
- Visibility control
- Active/paused states
- Update intervals
- Input Manager
- Input Bindings
- Input Types
- Camera class
- Asset Manager
- Image Asset

## What's New in v0.1.6

- Added Asset Manager
- Added Image Asset support
- Added image loading and caching
- Added image replacement and removal
- Added image reloading
- Bug fixes and general improvements

## Known Issues

- Mouse input coordinates are currently being worked on and may not behave correctly in some situations.

## Quick Start

```python
from pygame_foundation import Game, World, Entity
import pygame

game = Game(600, 500, "Pygame Foundation", 60)

world = game.world
input_manager = game.input_manager
camera = game.camera
assets = game.assets

entity = Entity(
    x=100,
    y=100,
    size=(50, 50)
)

def move_entity_right():
    entity.x += 10

world.add(entity)

input_manager.bind_key_pressed(
    move_entity_right,
    pygame.K_RIGHT
)

camera.follow(entity)

game.run()
```

## Roadmap

- Controller inputs
- Scene system
- Further camera features
- Additional asset types, such as sounds
- Animation system
- Timer system

## License

This project is licensed under the MIT License.