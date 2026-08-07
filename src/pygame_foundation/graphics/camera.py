from pygame_foundation.utils import debug_and_log
import pygame

class Camera:
    ''' A class to handle camera movements '''
    def __init__(self, position:tuple[int, int], window_width, window_height):
        ''' Initiliazes the Camera class '''
        self.position = pygame.Vector2(position)
        self._follow = None
        self.window_width = window_width
        self.window_height = window_height

    @property
    def x(self):
        return self.position.x

    @x.setter
    def x(self, value):
        self.position.x = value

    @property
    def y(self):
        return self.position.y

    @y.setter
    def y(self, value):
        self.position.y = value

    def move(self, dx, dy):
        ''' Move the camera. dx and dy are distance-x and -y '''
        self.x += dx
        self.y += dy

    def apply(self, rect):
        ''' Returns a rect with the camera position applied. '''
        return rect.move(-self.x, -self.y)

    def update(self):
        if self._follow is not None:
            self.position.update(
                self._follow.rect.centerx - self.window_width // 2,
                self._follow.rect.centery - self.window_height // 2,
            )

    def follow(self, sprite):
        ''' Makes the camera follow sprite.'''
        self._follow = sprite

    def stop_following(self):
        followed = self._follow
        self._follow = None
        return followed
    
