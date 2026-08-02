from pygame_foundation.utils.debug import debug_and_log
import pygame

class InputBinding:
    def __init__(self, key, func):
        ''' A class to store Input data '''
        self.key = key
        self.func = func

    def __call__(self, *args, **kwds):
        self.func()

class InputManager:
    def __init__(self):
        ''' A Manager for Keyboard Inputs '''
        self.inputs = {}

    def add_input_pdown(self, name, key, func):
        ''' Add a listener for when the key is pressed down. '''
        _input = InputBinding(key, func)
        if name in self.inputs:
            self.inputs[name].append(_input)
            return 

        self.inputs[name] =[_input]
            

    def update(self, events):
        keys = pygame.key.get_pressed()
        for name in self.inputs:
            for _input in self.inputs[name]:
                if keys[_input.key]:
                    _input()