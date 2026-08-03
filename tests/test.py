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

def go_berserk():
    for entity in world.sprites():
        entity.coordinates = (random.randint(0, 18)*50, random.randint(0, 13)*50)

def add_entity():
    x, y = (random.randint(0, 18)*50, random.randint(0, 13)*50)
    size = (random.randint(1, 3)*50, random.randint(1, 3)*50)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),)
    entity = Entity(x, y, size=size, color=color, )
    world.add(entity)

def remove_entity():
    if not world.sprites():
        for i in range(1):
            add_entity()
    entity = random.choice(world.sprites())
    world.remove(entity)

world.add(e4, e2, e3, e1)
input_manager.bind_key_held(pygame.K_w, move_up)
input_manager.bind_key_held(pygame.K_d, move_right)
input_manager.bind_key_held(pygame.K_s, move_down)
input_manager.bind_key_held(pygame.K_a, move_left)
input_manager.bind_key_pressed(pygame.K_SPACE, go_berserk)
input_manager.bind_key_release(pygame.K_EQUALS, add_entity) 
input_manager.bind_key_pressed(pygame.K_MINUS, remove_entity) 

if __name__ == '__main__':
    game.run()