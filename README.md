# pygame-foundation

A foundation for building Pygame projects and games.

pygame-foundation is currently in active development. Additional features are planned for future versions.
The current version is 0.1.4. In this version mouse inputs have been added, In addition to unbinding inputs
and clearing all bound inputs.

## Installation

pip install pygame-foundation

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

## Updates
- Input Listeners for mouse events including clicked, released, held and motion
- Input Types(UPDATED)
- Input Bindings(UPDATED)
- Input Manager(UPDATED)
- Unbinding
- Clearing All Inputs
- Activation and Deactivation of single Inputs

## Bug Fixes
- Removed debug and log from game.run
- Removed debug and log from binding methods

## Quick Start

```python
from pygame_foundation import Game, World, Entity
import pygame

game = Game(600, 500, 'Pygame Foundation', 60)
world = game.world
input_manager = game.input_manager

entity = Entity(
    x=100,
    y=100,
    size=(50, 50)
)

def move_entity_right():
    entity.x += 10

world.add(entity)
input_manager.bind_key_pressed(move_entity_right, pygame.K_RIGHT)

game.run()
```

## Roadmap

- Controller Inputs
- Scene system
- Camera
- Asset manager
- Animation system
- Timer system

## License

This project is licensed under the MIT License.

