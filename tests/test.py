from pygame_foundation.core import Entity, Game, World
from pygame_foundation.scene import Scene
import pygame

class GameScene(Scene):
    def __init__(self, game, name):
        super().__init__(game, name)
        self.world = World(game.camera)  
        self.counter = 0

    def update(self, dt, events):
        print(f'Game: {self.counter}')
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
        print('Pause')
        if self.is_active:
            self.world.update(dt)
        return

    def draw(self, screen):
        self.world.draw(screen)

game = Game(1000, 800, 'Test', 60, (0, -100))
input_manager = game.input_manager
camera = game.camera
assets = game.assets

game_scene = GameScene(game, 'GameScene')
pause_menu = PauseScene(game, 'PauseMenu')
scene_manager = game.scene_manager
scene_manager.change_scene(game_scene)

player_image = assets.load_image('player', 'tests\\image.png')
player = Entity(500, 100, player_image, layer=1)
e1 = Entity(300, 400, size=(100, 60), color=(10, 123, 203))
e2 = Entity(200, 100, size=(150, 100), color=(160, 13, 213))
e3 = Entity(500, 180, size=(260, 150), color=(100, 13, 23))

game_scene.world.add(player, e1) 
pause_menu.world.add(e2, e3) 

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

# camera.follow(player)

if __name__ == '__main__':
    game.run()