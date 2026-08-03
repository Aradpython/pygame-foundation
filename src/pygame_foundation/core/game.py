from pygame_foundation.input.manager import InputManager
from pygame_foundation.utils.debug import debug_and_log
from .constants import *
from .world import World
import pygame


class Game:
    ''' A class that acts as a manager for all events in the game '''
    def __init__(self, window_width, window_height, caption, fps):
        ''' Initialize the Game class and pygame '''
        pygame.init()

        self.window_width = window_width
        self.window_height = window_height
        self.fps = fps

        self.surface = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption(caption)

        self.clock = pygame.time.Clock()

        self.world = World()

        self.input_manager = InputManager()

    def update(self, dt, events):
        ''' Update the Game '''
        self.input_manager.update(events)

        self.world.update(dt)

    def draw(self):
        ''' Draw and blit Objects to the screen '''
        self.world.draw(self.surface)

    @debug_and_log({
        'success':'Successfully closed game',
        'error':'Error has occured during game',
    })
    def run(self):
        ''' Run the Game '''
        self.running = True
        while self.running:
            dt = self.clock.tick(self.fps) / 1000.0

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.surface.fill((0, 12, 12))

            self.update(dt, events)

            self.draw()

            pygame.display.update()
        pygame.quit()
