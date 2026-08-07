from pygame_foundation.core import Entity, Game
import pygame

game = Game(1000, 800, 'Test', 60, (0, -100))
world = game.world
input_manager = game.input_manager
camera = game.camera
assets = game.assets

player_image = assets.load_image('player', 'tests\\image.png')
player = Entity(500, 100, player_image, layer=1)
e1 = Entity(300, 400, size=(100, 60), color=(10, 123, 203), layer=0)
e2 = Entity(200, 100, size=(150, 100), color=(160, 13, 213), layer=0)
e3 = Entity(500, 180, size=(260, 150), color=(100, 13, 23), layer=0)

world.add(e1, e2, e3, player)

def move_up():
    player.y -= 5
    # for entity in world.sprites():
    #     if random.randint(0, 20) == 0:
    #         entity.y -= 5
def move_down():
    player.y += 5
    # for entity in world.sprites():
    #     if random.randint(0, 20) == 0:
    #         entity.y += 5
def move_right():
    player.x += 5

    # for entity in world.sprites():
    #     if random.randint(0, 20) == 0:
    #         entity.x += 5
def move_left():
    player.x -= 5
    # for entity in world.sprites():
    #     if random.randint(0, 20) == 0:
    #         entity.x -= 5

input_manager.bind_key_held(move_up, pygame.K_w)
input_manager.bind_key_held(move_right, pygame.K_d)
input_manager.bind_key_held(move_down, pygame.K_s)
input_manager.bind_key_held(move_left, pygame.K_a)

camera.follow(player)

s = assets

if __name__ == '__main__':
    game.run()