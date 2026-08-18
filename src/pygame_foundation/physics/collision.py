from collections.abc import Callable
from enum import Enum


class CollisionState(Enum):
    ''' A Enum subclass used to store collision states. '''
    ENTERED = 0
    STAYING = 1
    EXITED = 2
    NONE = 3

class Collision:
    ''' A class used to store metadata for expected collisions. '''
    def __init__(self, entity1, entity2, only_when:CollisionState, func:Callable=None, resolve:bool=False, resolve_who=None):
        self.entity1 = entity1
        self.entity2 = entity2
        self.only_when = only_when
        self.state = CollisionState.NONE
        self.on_collision = func
        self._was_colliding = False
        self.resolve = resolve

        if resolve is True:
            self.resolve_who = resolve_who
            if resolve_who == self.entity1:
                self.not_resolve = self.entity2
            else:
                self.not_resolve = self.entity1

    def __call__(self, *args, **kwds):
        if self.on_collision is not None:
            self.on_collision(self, *args, **kwds)

class CollisionManager:
    ''' A class used to manage Collision checks '''
    def __init__(self):
        self.collisions = []

    def add_collision_check(self, entity1, entity2, only_when:CollisionState, callback:Callable, resolve:bool=False, resolve_who=None):
        ''' 
        Adds a collision check between two rectangles. 
        The callback must accept the collision obj in its parameters.
        The resolve parameter is used for when you don't want two entities overlapping.
        It will resolve their positions. resolve_who is to determine which entity to move during resolution.
        '''
        collision = Collision(entity1, entity2, only_when, callback, resolve, resolve_who)
        self.collisions.append(collision)
        return collision

    def _handle_resolution(self, collision):
        if collision.resolve is True:
            resolve_who = collision.resolve_who.rect
            not_resolve = collision.not_resolve.rect
            overlap_x = min(resolve_who.right, not_resolve.right) - max(
                resolve_who.left, not_resolve.left
            )    
            overlap_y = min(resolve_who.bottom, not_resolve.bottom) - max(
                resolve_who.top, not_resolve.top
            )
            
            if overlap_x < overlap_y:
                if resolve_who.centerx < not_resolve.centerx:
                    resolve_who.right = not_resolve.left
                else:
                    resolve_who.left = not_resolve.right
            else:
                if resolve_who.centery < not_resolve.centery:
                    resolve_who.bottom = not_resolve.top
                else:
                    resolve_who.top = not_resolve.bottom

    def update(self):
        ''' Updates and checks for any occuring collisions. '''
        for collision in self.collisions:
            entity1 = collision.entity1
            entity2 = collision.entity2
    
            can_collide = (
                entity2.collision_group in entity1.collision_mask
                and
                entity1.collision_group in entity2.collision_mask
            )
            is_colliding = (
                can_collide and entity1.rect.colliderect(entity2.rect)
            )
    
            if is_colliding:
                self._handle_resolution(collision)
                if collision._was_colliding:
                    collision.state = CollisionState.STAYING
                else:
                    collision.state = CollisionState.ENTERED
    
                if collision.state == collision.only_when:
                    collision()

                collision._was_colliding = True
    
            elif collision._was_colliding:
                collision.state = CollisionState.EXITED
    
                if collision.state == collision.only_when:
                    collision()
    
                collision._was_colliding = False

                


            
