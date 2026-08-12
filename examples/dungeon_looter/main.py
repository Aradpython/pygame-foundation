from pygame_foundation.physics.collision import CollisionState
from pygame_foundation.core import Game
from classes import *
import pygame
from pathlib import Path

game = Game(900, 800, 'Dungeon Looter', 60)
collision_manager = game.collision_manager
scene_manager = game.scene_manager
input_manager = game.input_manager
camera = game.camera
assets = game.assets

game_scene = GameScene(game, 'Game Scene')
scene_manager.change_scene(game_scene)

ASSETS = Path(__file__).with_name('assets')

def load_optional_image(name, filename):
    path = ASSETS / filename
    if path.exists():
        return assets.load_image(name, str(path))
    return None

player_image = load_optional_image('player', 'player.png')
coin_image = load_optional_image('coin', 'coin.png')
enemy_image = load_optional_image('enemy', 'enemy.png')

COIN_POSITIONS = [(120, 120), (410, 100), (730, 120), (120, 520), (720, 610)]
player = Player(60, 60, player_image, goal=len(COIN_POSITIONS))
player.layer = 1
game_scene.set_player(player)

# Each tuple is x, y, width, height.  Together they form the maze corridors.
WALL_LAYOUT = [
    (0, 0, 900, 25), (0, 775, 900, 25), (0, 0, 25, 800), (875, 0, 25, 800),
    (170, 25, 30, 185), (170, 290, 30, 260), (170, 630, 30, 145),
    (340, 25, 30, 330), (340, 435, 30, 340),
    (510, 190, 30, 370), (510, 640, 30, 135),
    (680, 25, 30, 300), (680, 405, 30, 370),
    (25, 210, 100, 30), (200, 210, 100, 30),
    (370, 355, 100, 30), (540, 355, 100, 30),
    (710, 325, 135, 30), (30, 550, 110, 30), (200, 550, 100, 30),
    (370, 600, 100, 30), (540, 600, 100, 30), (710, 600, 135, 30),
]
walls = [Wall(x, y, (width, height)) for x, y, width, height in WALL_LAYOUT]
coins = [Coin(x, y, coin_image) for x, y in COIN_POSITIONS]
enemies = [
    Enemy(235, 255, enemy_image, 1),
    Enemy(555, 570, enemy_image, -1),
    Enemy(730, 370, enemy_image, 1),
]
for enemy in enemies:
    enemy.layer = 1

def collect_coin(collision):
    player.collect_coin()
    coin = collision.entity2
    coin.visible = False
    coin.active = False
    if player.coins == player.goal:
        print('You escaped with all the loot! '*5)
        game.running = False

def caught_by_enemy(collision):
    player.return_to_spawn()

def enemy_hit_wall(collision):
    collision.entity1.turn_around()

input_manager.bind_key_held(game_scene.input_context, player.move_up, pygame.K_w)
input_manager.bind_key_held(game_scene.input_context, player.move_down, pygame.K_s)
input_manager.bind_key_held(game_scene.input_context, player.move_left, pygame.K_a)
input_manager.bind_key_held(game_scene.input_context, player.move_right, pygame.K_d)

game_scene.world.add(player, *walls, *coins, *enemies)

for wall in walls:
    collision_manager.add_collision_check(player, wall, CollisionState.ENTERED, callback=None, resolve=True, resolve_who=player)
    for coin in coins:
        collision_manager.add_collision_check(coin, wall, CollisionState.ENTERED, callback=None, resolve=True, resolve_who=coin)
    for enemy in enemies:
        collision_manager.add_collision_check(enemy, wall, CollisionState.ENTERED, enemy_hit_wall, resolve=True, resolve_who=enemy)

for coin in coins:
    collision_manager.add_collision_check(player, coin, CollisionState.ENTERED, collect_coin)

for enemy in enemies:
    collision_manager.add_collision_check(player, enemy, CollisionState.ENTERED, caught_by_enemy)


game.run()
