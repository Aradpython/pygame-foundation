from pygame_foundation.assets.manager import AssetManager
from pygame_foundation.input.manager import InputManager
from pygame_foundation.scene.manager import SceneManager
from pygame_foundation.utils.debug import debug_and_log
from pygame_foundation.graphics.camera import Camera
from .constants import *
import pygame


class Game:
    ''' A class that acts as a manager for all events in the game '''
    def __init__(self, window_width:int, window_height:int, caption:str, fps:int, camera_position:tuple[int, int]=(0, 0)):
        ''' Initialize the Game class and pygame '''
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


    def update(self, events):
        ''' Update the Game '''
        # self.input_manager.update(events)
        self.camera.update()

    def run(self):
        ''' Run the Game '''
        self.running = True
        while self.running:
            dt = self.clock.tick(self.fps) / 1000.0

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.surface.fill(BLACK)

            self.update(events)

            self.scene_manager.update(dt, events)
            self.scene_manager.draw(self.surface)

            pygame.display.update()
        pygame.quit()
