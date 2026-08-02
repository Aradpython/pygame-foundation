# pygame-foundation

A foundation for building Pygame projects and games.

pygame-foundation is currently in active development. Additional features are planned for future versions.

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

## Updates
- Input Manager
- Input Bindings

## Quick Start

```python
from pygame_foundation import Game, World, Entity

game = Game()
world = game.world

player = Entity(
    x=100,
    y=100,
    size=(50, 50)
)

world.add(player)

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

