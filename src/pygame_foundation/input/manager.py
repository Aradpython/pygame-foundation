from pygame_foundation.utils.debug import debug_and_log
from enum import Enum
import pygame


class InputType(Enum):
    PRESSED = 1
    RELEASED = 2
    HELD = 3

class InputBinding:
    def __init__(self, key, func, type:InputType):
        ''' A class to store Input data '''
        self.key = key
        self.func = func
        self.type = type

    def __call__(self, *args, **kwds):
        self.func()

class InputManager:
    def __init__(self):
        ''' A Manager for Keyboard Inputs '''
        self.inputs = []
        self._pressed = []
        self._released = []
        self._held = []

    @debug_and_log({
        'success':'Succussfully Bound Key',
        'error':'Key Binding Error',
    })
    def bind_key_pressed(self, key, func):
        ''' Add a listener for when the key is pressed down. '''
        input_binding = InputBinding(key, func, InputType.PRESSED)
        self.inputs.append(input_binding)
        self._pressed.append(input_binding)

    @debug_and_log({
        'success':'Succussfully Bound Key',
        'error':'Key Binding Error',
    })
    def bind_key_release(self, key, func):
        ''' Add a listener for when the key is released. '''
        input_binding = InputBinding(key, func, InputType.RELEASED)
        self.inputs.append(input_binding)
        self._released.append(input_binding)

    @debug_and_log({
        'success':'Succussfully Bound Key',
        'error':'Key Binding Error',
    })
    def bind_key_held(self, key, func):
        ''' Add a listener for when the key is held down. '''
        input_binding = InputBinding(key, func, InputType.HELD)
        self.inputs.append(input_binding)
        self._held.append(input_binding)

    def update(self, events):
        keys = pygame.key.get_pressed()
        for event in events:
            for input_binding in self._pressed:
                if input_binding.type == InputType.PRESSED and event.type == pygame.KEYDOWN:
                    if event.key == input_binding.key:
                        input_binding()

            for input_binding in self._released:
                if input_binding.type == InputType.RELEASED and event.type == pygame.KEYUP:
                    if event.key == input_binding.key:
                        input_binding()

        for input_binding in self._held:   
            if input_binding.type == InputType.HELD and keys[input_binding.key]:
                input_binding()
