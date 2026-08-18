# **Quick Start**

To get you started:

```python
from pygame_foundation.core import Game, Entity, World
from pygame_foundation.scene import Scene
import pygame

class GameScene(Scene):
    def __init__(self, game, name):
        super().__init__(game, name)
        self.world = World(game.camera)  

    def update(self, dt, events):
        if self.is_active:
            self.world.update(dt)
        return

    def draw(self, screen):
        self.world.draw(screen)

game = Game(
    600,
    500,
    "Pygame Foundation",
    60
)
input_manager = game.input_manager
scene_manager = game.scene_manager
camera = game.camera

game_scene = GameScene(game, 'GAME')
scene_manager.change_scene(game_scene)
world = game_scene.world


player = Entity(
    x=100,
    y=100,
    size=(50, 50)
)

entity = Entity(
    x=200, 
    y=200, 
    size=(50, 50),
    color=(100, 10, 1)
)


world.add(player, entity)


def move_right():
    player.x += 5

def move_left():
    player.x -= 5


input_manager.bind_key_held(
    game_scene.input_context,
    move_right,
    pygame.K_RIGHT
)

input_manager.bind_key_held(
    game_scene.input_context,
    move_left,
    pygame.K_LEFT
)

camera.follow(player)

game.run()

```

The code above creates screen with a player that is a white 50x50 rectangle that can move horizontally and a red entity as well as the fact that the camera follows the player. 