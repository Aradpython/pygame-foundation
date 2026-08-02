from .constants import UPDATE_EVERY_FRAME, WHITE, BLACK, GREEN
from .debug import debug_and_log
from termcolor import colored
import pygame
import random

class World(pygame.sprite.Group):
    """An enhanced Sprite Group used to manage game entities."""

    def __init__(self):
        super().__init__()
        print(colored('Info:', 'blue'), 'The Message above is normal even when no obj is added to the world')

        self._layers = {}
        self._priorities = {}
        self._tags = {}

    @debug_and_log(
        {
            'success':'Succussfully added obj/objs to World',
            'error':'World Obj Addition Error'
        }
    )
    def add(self, *sprites: pygame.sprite.Sprite) -> None:
        super().add(*sprites)

        for sprite in sprites:
            sprite._world = self

        self._update_layers(*sprites)
        self._update_priorities(*sprites)
        self._update_tags(*sprites)

    @debug_and_log(
        {
            'success':'Succussfully removed obj/objs from World',
            'error':'World Obj Removal Error'
        }
    )
    def remove(self, *sprites):
        super().remove(*sprites)

        for sprite in sprites:

            self._layers[sprite.layer].remove(sprite)
            self._priorities[sprite.priority].remove(sprite)

            if not self._layers[sprite.layer]:
                del self._layers[sprite.layer]

            if not self._priorities[sprite.priority]:
                del self._priorities[sprite.priority]

            for tag in sprite.tags:
                self._tags[tag].remove(sprite)
            
                if not self._tags[tag]:
                    del self._tags[tag]

            sprite._world = None

    def _update_tags(self, *sprites):
        for sprite in sprites:
            for tag in sprite.tags:
                self._tags.setdefault(tag, []).append(sprite)

    def _add_tag(self, sprite, tag):
        self._tags.setdefault(tag, []).append(sprite)

    def _remove_tag(self, sprite, tag):
        if tag in self._tags:
            self._tags[tag].remove(sprite)

            if not self._tags[tag]:
                del self._tags[tag]

    def _update_priorities(self, *sprites):
        for sprite in sprites:
            if sprite.priority in self._priorities:
                self._priorities[sprite.priority].append(sprite)

            else:
                self._priorities[sprite.priority] = [sprite]

    def _move_priority(self, sprite, old_priority, new_priority):
        self._priorities[old_priority].remove(sprite)

        if not self._priorities[old_priority]:
            del self._priorities[old_priority]

        self._priorities.setdefault(new_priority, []).append(sprite)

    def _update_layers(self, *sprites):
        for sprite in sprites:
            if sprite.layer in self._layers:
                self._layers[sprite.layer].append(sprite)

            else:
                self._layers[sprite.layer] = [sprite]

    def _move_layer(self, sprite, old_layer, new_layer):
        # Remove from old layer
        self._layers[old_layer].remove(sprite)

        # Delete empty layer
        if not self._layers[old_layer]:
            del self._layers[old_layer]

        # Add to new layer
        self._layers.setdefault(new_layer, []).append(sprite)

    def _find_tags(self, *tags, match_all=False):
        sprites = []
        matcher = all if match_all else any

        for sprite in self.sprites():
            if matcher(tag in sprite._tags for tag in tags):
                sprites.append(sprite)

        return sprites

    def draw(self, surface):
        for layer in sorted(self._layers):
            for sprite in self._layers[layer]:
                if not sprite.active:
                    continue

                sprite.draw(surface)

    def update(self, dt):
        ''' Updates the objects in the world according to their update_interval and priority. '''
        for priority in sorted(self._priorities):
            for sprite in self._priorities[priority]:
                if not sprite.active or sprite.paused:
                    continue

                sprite._elapsed += dt

                if sprite.update_interval is UPDATE_EVERY_FRAME:
                    sprite.update(dt)

                elif sprite._elapsed >= sprite.update_interval:
                    sprite.update(dt)
                    sprite._elapsed -= sprite.update_interval

    @debug_and_log({
            'success':'Succussfully found sprites by tags',
            'error':'Sprites Search by Tags Error'
        }
    )
    def find_by_tags(self, *tags) -> list:
        ''' 
        Gets all the sprites that contains the specified tags.
        This function gets all the sprites that contain any of the tags
        not filter them by tags.
        '''
        sprites = []

        for tag in tags:
            for sprite in self._tags.get(tag, []):
                if sprite not in sprites:
                    sprites.append(sprite)

        return sprites

    @debug_and_log({
            'success':'Succussfully found sprites by tags',
            'error':'Sprites Search by Tags(Match All) Error'
        }
    )
    def find_by_tags_all(self, *tags) -> list:
        ''' 
        Gets all the sprites that contains the specified tags.
        This function filters and gets all the sprites that have all the tags
        not only one.
        '''
        sprites = set(self._tags.get(tags[0], []))
        for tag in tags[1:]:
            sprites &= set(self._tags.get(tag, []))

        return list(sprites)

    @debug_and_log(
        {
            'success':'Succussfully paused sprites by tags',
            'error':'Sprites Pause by Tags Error'
        }
    )
    def pause_tags(self, *tags) -> list:
        ''' 
        Pauses the sprites that contains the specified tags.
        It does this by changing the paused attribute on the entity to True.
        '''
        sprites = self._find_tags(*tags)
        for sprite in sprites:
            sprite.paused = True

        return sprites

    @debug_and_log(
        {
            'success':'Succussfully resumed sprites by tags',
            'error':'Sprites Resume by Tags Error'
        }
    )
    def resume_tags(self, *tags) -> list:
        ''' 
        Resumes the sprites that contains the specified tags.
        It does this by changing the paused attribute on the entity to False.
        '''
        sprites = self._find_tags(*tags)
        for sprite in sprites:
            sprite.paused = False

        return sprites

    @debug_and_log(
        {
            'success':'Succussfully hid sprites by tags',
            'error':'Sprites Hide by Tags Error'
        }
    )
    def hide_tags(self, *tags) -> list:
        ''' 
        Hides the sprites that contains the specified tags.
        It does this by changing the visible attribute on the entity to False.
        '''
        sprites = self._find_tags(*tags)
        for sprite in sprites:
            sprite.visible = False
        
        return sprites

    @debug_and_log(
        {
            'success':'Succussfully shown sprites by tags',
            'error':'Sprites Show by Tags Error'
        }
    )
    def show_tags(self, *tags) -> list:
        ''' 
        Show the hidden sprites that contains the specified tags.
        It does this by changing the visible attribute on the entity to True.
        '''
        sprites = self._find_tags(*tags)
        for sprite in sprites:
            sprite.visible = True
        
        return sprites

    @debug_and_log(
        {
            'success':'Succussfully activated sprites by tags',
            'error':'Sprites Activation by Tags Error'
        }
    )
    def activate_tags(self, *tags) -> list:
        ''' 
        Activate the sprites that contains the specified tags.
        It does this by changing the active attribute on the entity to True.
        '''
        sprites = self._find_tags(*tags)
        for sprite in sprites:
            sprite.active = True
        
        return sprites

    @debug_and_log(
        {
            'success':'Succussfully deactivated sprites by tags',
            'error':'Sprites Deactivation by Tags Error'
        }
    )
    def deactivate_tags(self, *tags) -> list:
        ''' 
        Deactivate the sprites that contains the specified tags.
        It does this by changing the active attribute on the entity to False.
        '''
        sprites = self._find_tags(*tags)
        for sprite in sprites:
            sprite.active = False

        return sprites
        