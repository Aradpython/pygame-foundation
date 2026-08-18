from enum import Enum

class SceneStatus(Enum):
    ''' A Enum subclass used to store Scene States'''
    ACTIVE = 0
    PAUSED = 1
    INACTIVE = 2

class Scene:
    ''' A class ment to be used as a super class. It is for creating different scenes. '''
    def __init__(self, game, name:str):
        self.game = game
        self.name = name
        self.status = SceneStatus.INACTIVE
        self.input_context = game.input_manager.create_context(name)
        self.blocks_updates = True
        self.blocks_drawings = False

    @property
    def is_active(self):
        ''' Return whether the scene is active or not. '''
        return self.status is SceneStatus.ACTIVE

    def enter(self):
        ''' Enter a Scene. Used as part of the scene lifecycle. Will change the scene status.'''
        self.status = SceneStatus.ACTIVE

    def exit(self):
        ''' Exits a Scene. Used as part of the scene lifecycle. Will change the scene status.'''
        self.status = SceneStatus.INACTIVE

    def update(self, dt):
        ''' Updates every frame. Overide in subclasses. '''
        pass

    def draw(self, screen):
        ''' Draws every frame. Overide in subclasses '''
        pass

    def pause(self):
        ''' Pauses a Scene. Used as part of the scene lifecycle. Will change the scene status.'''
        self.status = SceneStatus.PAUSED

    def resume(self):
        ''' 
        Resumes a Scene. Used as part of the scene lifecycle. 
        Will change the scene status. Only takes effect when the scene is entered.
        '''
        if self.status is not SceneStatus.INACTIVE:
            self.status = SceneStatus.ACTIVE
