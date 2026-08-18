from pygame_foundation.physics.collision import CollisionManager
from pygame_foundation.assets.manager import AssetManager
from pygame_foundation.input.manager import InputManager
from pygame_foundation.scene.manager import SceneManager
from pygame_foundation.utils.debug import debug_and_log
from pygame_foundation.graphics.camera import Camera
from .timer import TimerManager
from .constants import *
import pygame



class Game:
    ''' A class that acts as a manager for all events in the game.  '''
    def __init__(self, window_width:int, window_height:int, caption:str, fps:int, camera_position:tuple[int, int]=(0, 0)):
        ''' Initializes the Game class and pygame. As well as all the Managers and Camera. '''
        pygame.init()

        self.window_width = window_width
        self.window_height = window_height
        self.fps = fps

        self.surface = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption(caption)

        self.clock = pygame.time.Clock()

        self.camera = Camera(camera_position, window_width, window_height)
        self.assets = AssetManager()
        self.scene_manager = SceneManager(self)
        self.input_manager = InputManager()
        self.collision_manager = CollisionManager()
        self.timer_manager = TimerManager()

    def update(self, dt, events):
        ''' Updates the Game '''
        self.timer_manager.update(dt)
        self.camera.update()
        self.scene_manager.update(dt, events)
        self.collision_manager.update()

    def run(self):
        ''' Runs the Game '''
        self.running = True
        while self.running:
            dt = self.clock.tick(self.fps) / 1000.0

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.surface.fill(BLACK)

            self.update(dt, events)

            self.scene_manager.draw(self.surface)
            pygame.display.update()

        pygame.quit()
