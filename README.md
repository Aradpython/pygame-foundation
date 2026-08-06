# pygame-foundation

A foundation for building Pygame projects and games.

pygame-foundation is currently in active development. Additional features are planned for future versions.
The latest version is 0.1.5. In this version camera functionality has been added.

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
- Camera Class


## Updates
- Camera class 
- Drawing updates
- camera.apply()
- camera.follow()
- camera.stop_following() 

## Bug to be fixed
- mouse input coordinates to be fixed

## Quick Start

```python
from pygame_foundation import Game, World, Entity
import pygame

game = Game(600, 500, 'Pygame Foundation', 60)
world = game.world
input_manager = game.input_manager
camera = game.camera

entity = Entity(
    x=100,
    y=100,
    size=(50, 50)
)

def move_entity_right():
    entity.x += 10

world.add(entity)
input_manager.bind_key_pressed(move_entity_right, pygame.K_RIGHT)
camera.follow(entity)

game.run()
```

## Roadmap

- Controller Inputs
- Scene system
- Further camera features
- Asset manager
- Animation system
- Timer system

## License

This project is licensed under the MIT License.

