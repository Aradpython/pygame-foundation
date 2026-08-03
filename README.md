# pygame-foundation

A foundation for building Pygame projects and games.

pygame-foundation is currently in active development. Additional features are planned for future versions.
The current version is 0.1.3.

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
- Input Listeners for Held/Pressed/Released
- Input Types

## Quick Start

```python
from pygame_foundation import Game, World, Entity

game = Game()
world = game.world
input_manager = game.input_manager

entity = Entity(
    x=100,
    y=100,
    size=(50, 50)
)

world.add(entity)

game.run()
```

## Roadmap

- Scene system
- Camera
- Asset manager
- Animation system
- Timer system

## License

This project is licensed under the MIT License.

