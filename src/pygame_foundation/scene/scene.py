from enum import Enum

class SceneStatus(Enum):
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
        return self.status is SceneStatus.ACTIVE

    def enter(self):
        self.status = SceneStatus.ACTIVE

    def exit(self):
        self.status = SceneStatus.INACTIVE

    def update(self, dt):
        ''' Overide in subclasses '''

    def draw(self, screen):
        ''' Overide in subclasses '''

    def pause(self):
        self.status = SceneStatus.PAUSED

    def resume(self):
        if self.status is not SceneStatus.INACTIVE:
            self.status = SceneStatus.ACTIVE
