from pygame_foundation.utils.debug import debug_and_log
from .constants import WHITE, UPDATE_EVERY_FRAME
from pygame_foundation.assets.manager import ImageAsset
from pygame import Surface
import pygame 

class Entity(pygame.sprite.Sprite):
    ''' A super class to be used to create subclasses  '''
    def __init__(self,
                x,
                y,
                image:Surface=None, 
                size=(0, 0), 
                color=WHITE, 
                visible:bool=True,
                paused:bool=False,
                active:bool=True,
                priority:int=0,
                layer:int=0,
                update_interval:float=UPDATE_EVERY_FRAME,
                tags:set=None,
                name='Entity'):
        ''' Initializes the Entity Class '''
        super().__init__()
        if image :
            self.image = image
            self.rect = self.image.get_rect(topleft=(x, y))


        else:
            self.image = None
            self.rect = pygame.Rect(x, y, *size)
            self.color = color
            self.size = size

        self._world = None

        self.visible = visible
        self.paused = paused
        self.active = active
        self._priority = priority
        self._layer = layer
        self.update_interval = update_interval
        self._elapsed = 0.0
        self._tags = set() if tags is None else set(tags)
        self.name = name

    def __str__(self):
        return self.name

    @property
    def coordinates(self):
        return self.rect.topleft

    @coordinates.setter
    def coordinates(self, value):
        self.rect.topleft = value

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, value):
        self.rect.x = value

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, value):
        self.rect.y = value

    @property
    def world(self):
        return self._world

    @property
    def tags(self): 
        return frozenset(self._tags)
    
    @property
    def layer(self):
        return self._layer

    @layer.setter
    def layer(self, value):
        if self._layer == value:
            return

        old_layer = self._layer
        self._layer = value

        if self._world is not None:
            self._world._move_layer(self, old_layer, value)

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if self._priority == value:
            return

        old_priority = self._priority
        self._priority = value

        if self._world is not None:
            self._world._move_priority(self, old_priority, value)

    def update(self, dt):
       '''Override in subclasses'''
       pass

    def draw(self, surface, camera):
        ''' Draw or blit self to screen '''
        if self.visible:

            if self.image:
                surface.blit(self.image, camera.apply(self.rect))

            else:
                pygame.draw.rect(surface, self.color, camera.apply(self.rect))

    @debug_and_log({
        'success':'Succussfully added tag.',
        'error':'Tag Addition Error',
    })
    def add_tag(self, tag):
        if tag in self._tags:
            return

        self._tags.add(tag)

        if self._world is not None:
            self._world._add_tag(self, tag)

    @debug_and_log({
        'success':'Succussfully removed tag.',
        'error':'Tag Removal Error',
    })
    def remove_tag(self, tag):
        if tag not in self._tags:
            return

        self._tags.remove(tag)

        if self._world is not None:
            self._world._remove_tag(self, tag)

    def has_tag(self, tag):
        return tag in self._tags