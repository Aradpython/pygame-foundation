from pygame_foundation.utils.debug import debug_and_log
from .constants import WHITE, UPDATE_EVERY_FRAME
from pygame import Surface
import pygame 

class Entity(pygame.sprite.Sprite):
    ''' A class ment to be used instead of the pygame.sprite.Sprite . '''
    def __init__(self,
                x,
                y,
                image:Surface=None, 
                size=(0, 0), 
                color:tuple[int, int, int]=WHITE, 
                visible:bool=True,
                paused:bool=False,
                active:bool=True,
                priority:int=0,
                layer:int=0,
                update_interval:float=UPDATE_EVERY_FRAME,
                tags:set=None,
                name:str='Entity',
                collision_group:str='None',
                collision_mask:set[str]=None
                ):
        ''' 
        Initializes the Entity.

        IMPORTANT: All entities that require a collision check must have the other in the collision mask.
        
        For instance:
            player = Entity(collision_group='PLAYER', collision_mask={'COIN'})
            player = Entity(collision_group='COIN', collision_mask={'PLAYER'})
        
        NOT:
            player = Entity(collision_group='PLAYER', collision_mask={'COIN'})
            player = Entity(collision_group='COIN', collision_mask={})
        '''
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

        self.collision_group = collision_group
        self.collision_mask = set() if collision_mask is None else set(collision_mask)

    def __str__(self):
        return self.name

    @property
    def coordinates(self):
        ''' The entity's world coordinates '''
        return self.rect.topleft

    @coordinates.setter
    def coordinates(self, value):
        ''' The entity's world coordinates '''
        self.rect.topleft = value

    @property
    def x(self):
        ''' The entity's x world coordinates '''
        return self.rect.x

    @x.setter
    def x(self, value):
        ''' The entity's x world coordinates '''
        self.rect.x = value

    @property
    def y(self):
        ''' The entity's y world coordinates '''
        return self.rect.y

    @y.setter
    def y(self, value):
        ''' The entity's y world coordinates '''
        self.rect.y = value

    @property
    def world(self):
        ''' The World class that the Entity belongs to. '''
        return self._world

    @property
    def tags(self): 
        ''' A frozen set of the tags the Entity owns. '''
        return frozenset(self._tags)
    
    @property
    def layer(self):
        ''' The layer the Entity should be drawn. Also known as the z-index. '''
        return self._layer

    @layer.setter
    def layer(self, value):
        ''' The layer the Entity should be drawn. Also known as the z-index. '''
        if self._layer == value:
            return

        old_layer = self._layer
        self._layer = value

        if self._world is not None:
            self._world._move_layer(self, old_layer, value)

    @property
    def priority(self):
        ''' The update priority of the Entity. '''
        return self._priority

    @priority.setter
    def priority(self, value):
        ''' The update priority of the Entity. '''
        if self._priority == value:
            return

        old_priority = self._priority
        self._priority = value

        if self._world is not None:
            self._world._move_priority(self, old_priority, value)

    def update(self, dt):
       '''A method that is run automatically depending on the update interval. Override in subclasses'''
       pass

    def draw(self, surface, camera):
        ''' Draw or blit self to screen. Is automatically called depending on the update interval. '''
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
        ''' Add a tag to the Entity '''
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
        ''' Remove a tag from the Entity '''
        if tag not in self._tags:
            return

        self._tags.remove(tag)

        if self._world is not None:
            self._world._remove_tag(self, tag)

    def has_tag(self, tag):
        ''' Checks if the tag exists in the Entity. Returns a boolean. '''
        return tag in self._tags