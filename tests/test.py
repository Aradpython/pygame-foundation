## EPILEPSY WARNING ##

from pygame_foundation.core import Entity, Game
from pygame_foundation.input import InputType
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
    for entity in world.sprites():
        entity.y -= 5

def move_down():
    for entity in world.sprites():
        entity.y += 5

def move_right():
    for entity in world.sprites():
        entity.x += 5

def move_left():
    for entity in world.sprites():
        entity.x -= 5

def go_berserk(event):
    for entity in world.sprites():
        entity.coordinates = (random.randint(0, 18)*50, random.randint(0, 13)*50)

def add_entity():
    x, y = (random.randint(0, 18)*50, random.randint(0, 13)*50)
    size = (random.randint(1, 3)*50, random.randint(1, 3)*50)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    entity = Entity(x, y, size=size, color=color, )
    world.add(entity)

def remove_entity():
    if not world.sprites():
        return 
    entity = random.choice(world.sprites())
    world.remove(entity)

def move_all(x, y):
    for e in world.sprites():
        e.coordinates = input_manager.mouse_position
        e.layer = random.randint(0, 10)

def color():
    for e in world.sprites():
        e.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

world.add(e4, e2, e3, e1)
b = input_manager.bind_key_held(move_up, pygame.K_w)
input_manager.bind_key_held(move_right, pygame.K_d)
input_manager.bind_key_held(move_down, pygame.K_s)
input_manager.bind_key_held(move_left, pygame.K_a)
input_manager.bind_mouse_held(move_all, pygame.BUTTON_LEFT)
input_manager.bind_mouse_clicked(go_berserk, pygame.BUTTON_LEFT)
input_manager.bind_mouse_clicked(go_berserk, pygame.BUTTON_WHEELUP)
input_manager.bind_mouse_clicked(go_berserk, pygame.BUTTON_WHEELDOWN)
input_manager.bind_key_release(add_entity, pygame.K_EQUALS)
input_manager.bind_key_pressed(remove_entity, pygame.K_MINUS)
input_manager.bind_key_pressed(color, None)


if __name__ == '__main__':
    game.run()