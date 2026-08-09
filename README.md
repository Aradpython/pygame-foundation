# pygame-foundation

A foundation for building Pygame projects and games.

`pygame-foundation` provides reusable systems and abstractions for building Pygame games without having to implement common game-engine functionality from scratch.

The project is currently in active development, with additional features planned for future releases.

**Latest version: 0.1.7**

## Installation

```bash
pip install pygame-foundation
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
- Keyboard input
- Mouse input
- Input contexts
- Scene-specific input contexts

### Camera

- Camera system
- Entity following
- Camera positioning

### Assets

- Asset Manager
- Image Assets
- Image loading
- Image metadata management

### Scenes

- Scene class
- Scene Manager
- Scene lifecycle
- Scene switching
- Scene stack
- Scene-specific input contexts
- Scene `enter()` / `exit()` lifecycle
- Scene `pause()` / `resume()` lifecycle
- Scene update blocking
- Scene drawing blocking
- Scene overlays

## What's New in 0.1.7

### Scene Management

Version `0.1.7` introduces a scene management system for organizing different parts of a game such as menus, gameplay, pause screens, settings, and other game states.

Scenes support a lifecycle consisting of:

```text
enter()
exit()
pause()
resume()
```

### Scene Stack

Scenes can now be stacked using:

```python
scene_manager.push_scene(scene)
```

and removed using:

```python
scene_manager.pop_scene()
```

This makes it possible to create structures such as:

```text
GameScene
    ↓
PauseScene
    ↓
SettingsScene
```
The underlying scenes can remain preserved while another scene is active.

You can also completely replace the current scene with:

```python
scene_manager.change_scene(scene)
```

### Scene Input Contexts

Each scene can have its own input context.

This allows different scenes to respond to different inputs.

For example:

```text
GameScene
    → WASD movement

PauseScene
    → Mouse/menu controls
```

When the active scene changes, the corresponding input context is automatically activated.

### Scene Update & Drawing Control

Scenes can control whether they block scenes underneath them from updating or drawing.

This allows overlays such as pause menus while keeping the underlying game visible.

For example:

```python
pause_scene.blocks_updates = True
pause_scene.blocks_drawings = False
```

This allows the game to remain visible while its updates are paused.

## Quick Start

```python
import pygame

from pygame_foundation import Game, World, Entity
from pygame_foundation.scene import Scene


class GameScene(Scene):
    def __init__(self, game, name):
        super().__init__(game, name)
        self.world = World(game.camera)

    def update(self, dt, events):
        self.world.update(dt)

    def draw(self, screen):
        self.world.draw(screen)


class PauseScene(Scene):
    def __init__(self, game, name):
        super().__init__(game, name)

        self.blocks_updates = True
        self.blocks_drawings = False

    def update(self, dt, events):
        pass

    def draw(self, screen):
        pass


game = Game(600, 500, "Pygame Foundation", 60)

scene_manager = game.scene_manager

game_scene = GameScene(game, "GameScene")
pause_scene = PauseScene(game, "PauseScene")

scene_manager.change_scene(game_scene)

# Later:
scene_manager.push_scene(pause_scene)

# To return:
scene_manager.pop_scene()

game.run()
```

## Roadmap

Planned features include:

- Controller / joystick input
- Further camera features
- Further asset types, such as sounds
- Animation system
- Timer system
- Additional scene features
- Additional input features

## Development

`pygame-foundation` is currently under active development.

The API may change between early releases as the framework continues to evolve.

## License

This project is licensed under the MIT License.