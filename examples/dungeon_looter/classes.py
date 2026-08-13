from pygame_foundation.core import World, Entity
from pygame_foundation.scene import Scene
import pygame

class GameScene(Scene):
    def __init__(self, game, name):
        super().__init__(game, name)
        self.world = World(self.game.camera)
        self.input_context = game.input_manager.create_context('Game')
        self.player = None
        self.font = pygame.font.Font(None, 32)

    def set_player(self, player):
        self.player = player

    def update(self, dt, events):
        self.world.update(dt)

    def draw(self, screen):
        self.world.draw(screen)
        if self.player is not None:
            score = self.font.render(f'Loot: {self.player.coins}', True, (255, 230, 90))
            help_text = self.font.render('WASD: move   Avoid the red guards!', True, (235, 235, 235))
            screen.blit(score, (20, 18))
            screen.blit(help_text, (20, 50))


class Player(Entity):
    def __init__(self, x, y, image=None):
        super().__init__(x, y, image)
        self.collision_group = 'PLAYER'
        self.collision_mask = {'WALL', 'COIN', 'ENEMY'}
        self.coins = 0
        self.velocity = 5
        self.spawn_point = (x, y)

    def move_up(self):
        self.y -= self.velocity
    
    def move_down(self):
        self.y += self.velocity

    def move_left(self):
        self.x -= self.velocity
    
    def move_right(self):
        self.x += self.velocity

    def collect_coin(self):
        self.coins += 1

    def return_to_spawn(self):
        self.coordinates = self.spawn_point

class Wall(Entity):
    def __init__(self, x, y,  size=(0, 0)):
        super().__init__(x, y, size=size, color=(125, 125, 125))
        self.collision_group = 'WALL'
        self.collision_mask = {'PLAYER', 'COIN', 'ENEMY'}


class Coin(Entity):
    def __init__(self, x, y, image=None):
        super().__init__(x, y, image=image, size=(25, 25), color=(255, 220, 0), name='coin')
        self.collision_group = 'COIN'
        self.collision_mask = {'PLAYER', 'WALL'}

class Enemy(Entity):
    def __init__(self, x, y, image=None, direction=1):
        super().__init__(x, y, image=image, size=(30, 30), color=(210, 60, 65), name='enemy')
        self.collision_group = 'ENEMY'
        self.collision_mask = {'PLAYER', 'WALL'}
        self.direction = direction
        self.speed = 5

    def update(self, dt):
        self.x += self.speed * self.direction

    def turn_around(self):
        self.direction *= -1
