from pygame_foundation.core import Entity, Game
import pygame
import random

game = Game(1000, 800, 'Test', 60)
world = game.world
input_manager = game.input_manager

e1 = Entity(500, 100, size=(100, 150), color=(10, 123, 23), layer=-10, tags=set(['cool', 'block']), name='Green Block')
e2 = Entity(200, 100, size=(150, 100), color=(160, 13, 213), layer=5, tags=set(['stupid', 'block', 'hidden']), name='Purple Block', visible=True)
e3 = Entity(500, 180, size=(260, 150), color=(100, 13, 23), layer=0, tags=set(['player', 'cool', 'hidden']), name='Player 1', visible=True)
e4 = Entity(300, 400, size=(100, 60), color=(10, 123, 203), layer=0, tags=set(['player', 'stupid']), name='Player 2')

def move_up():
    e1.y -= 5
    e2.y -= 5
    e3.y -= 5
    e4.y -= 5

def move_down():
    e1.y += 5
    e2.y += 5
    e3.y += 5
    e4.y += 5

def move_right():
    e1.x += 5
    e2.x += 5
    e3.x += 5
    e4.x += 5

def move_left():
    e1.x -= 5
    e2.x -= 5
    e3.x -= 5
    e4.x -= 5

def go_breserk():
    e1.coordinates = (random.randint(0, 18)*50, random.randint(0, 13)*50)
    e2.coordinates = (random.randint(0, 18)*50, random.randint(0, 13)*50)
    e3.coordinates = (random.randint(0, 18)*50, random.randint(0, 13)*50)
    e4.coordinates = (random.randint(0, 18)*50, random.randint(0, 13)*50)

world.add(e4, e2, e3, e1)
input_manager.add_input_pdown('Up', pygame.K_w, move_up)
input_manager.add_input_pdown('Right', pygame.K_d, move_right)
input_manager.add_input_pdown('Down', pygame.K_s, move_down)
input_manager.add_input_pdown('Left', pygame.K_a, move_left)
input_manager.add_input_pdown('breserk', pygame.K_SPACE, go_breserk)

if __name__ == '__main__':
    game.run()