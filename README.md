# pygame-foundation

A foundation for building Pygame projects and games.

pygame-foundation is currently in active development. Version 0.1.1 is the initial public release, and additional features are planned for future versions.

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
- Input manager
- Asset manager
- Animation system
- Timer system


## License

This project is licensed under the MIT License.

