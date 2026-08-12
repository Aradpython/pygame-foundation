from pygame_foundation.physics.collision import CollisionState
from pygame_foundation.core import Entity, Game, World
from pygame_foundation.scene import Scene
import pygame
import random

class GameScene(Scene):
    def __init__(self, game, name):
        super().__init__(game, name)
        self.world = World(game.camera)  
        self.counter = 0

    def update(self, dt, events):
        self.counter += 1
        if self.is_active:
            self.world.update(dt)
        return

    def draw(self, screen):
        self.world.draw(screen)

class PauseScene(Scene):
    def __init__(self, game, name):
        super().__init__(game, name)
        self.world = World(game.camera)
        
    def update(self, dt, events):
        if self.is_active:
            self.world.update(dt)
        return

    def draw(self, screen):
        self.world.draw(screen)

coins = 0

game = Game(1000, 800, 'Test', 60, (0, -50))
input_manager = game.input_manager
camera = game.camera
assets = game.assets
scene_manager = game.scene_manager
collision_manager = game.collision_manager

pause_menu = PauseScene(game, 'PauseMenu')
game_scene = GameScene(game, 'GameScene')
scene_manager.change_scene(game_scene)

player_image = assets.load_image('player', 'tests\\image.png')

player = Entity(500, 100, player_image, layer=1, name='Player', collision_group='PLAYER', collision_mask={'COIN', 'CONVEYOR', 'WALL'})
coin = Entity(300, 400, size=(100, 60), color=(10, 123, 203), collision_group='COIN', collision_mask={'PLAYER'})
wall = Entity(100, 100, size=(25, 500), color=(255, 255, 255), collision_group='WALL', collision_mask={'PLAYER'})
conveyor = Entity(500, 100, size=(50, 300), color=(50, 50, 50), collision_group='CONVEYOR', collision_mask={'PLAYER'})
e2 = Entity(200, 100, size=(150, 100), color=(160, 13, 213), collision_group='PAUSE BLOCK')
e3 = Entity(500, 180, size=(260, 150), color=(100, 13, 23), collision_group='PAUSE BLOCK')

game_scene.world.add(player, coin, wall, conveyor) 
pause_menu.world.add(e2, e3) 

def move_coin_randomly(collision):
    global coins
    coin.x = random.randint(0, game.window_width - 100)
    coin.y = random.randint(0, game.window_height - 100)
    coins += 1
    print(f'Coins: {coins}')

def conveyor_p_move(collision):
    collision.entity1.y -= 4

collision_manager.add_collision_check(player, coin, CollisionState.ENTERED, move_coin_randomly)
collision_manager.add_collision_check(player, wall, CollisionState.ENTERED, None, resolve=True, resolve_who=player)
collision_manager.add_collision_check(player, conveyor, CollisionState.STAYING, conveyor_p_move)


def move_up():
    player.y -= 5

def move_down():
    player.y += 5

def move_right():
    player.x += 5

def move_left():
    player.x -= 5

def change_scene_to_game(event):
    scene_manager.pop_scene()

def change_scene_to_pause(event):
    scene_manager.push_scene(pause_menu)


input_manager.bind_key_held(game_scene.input_context, move_up, pygame.K_w)
input_manager.bind_key_held(game_scene.input_context, move_right, pygame.K_d)
input_manager.bind_key_held(game_scene.input_context, move_down, pygame.K_s)
input_manager.bind_key_held(game_scene.input_context, move_left, pygame.K_a)
input_manager.bind_mouse_clicked(game_scene.input_context, change_scene_to_pause, pygame.BUTTON_LEFT)
input_manager.bind_mouse_clicked(pause_menu.input_context, change_scene_to_game, pygame.BUTTON_RIGHT)


if __name__ == '__main__':
    game.run()