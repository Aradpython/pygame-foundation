from pygame_foundation.utils.debug import debug_and_log
from typing import dataclass_transform
from enum import Enum
import pygame


class InputType(Enum):
    KEY_PRESSED = 1
    KEY_RELEASED = 2
    KEY_HELD = 3
    MOUSE_CLICKED = 4
    MOUSE_RELEASED = 5
    MOUSE_HELD = 6
    MOUSE_MOTION = 7

class InputBinding:
    def __init__(self, key_btn, func, type:InputType, mouse=False, is_active=True):
        ''' A class to store Input data '''
        self.func = func
        self.type = type
        if key_btn is None:
            self.any_input = True

        else:
            self.any_input = False
        
        if mouse:
            self.button = key_btn
            self.key = None

        else:
            self.key = key_btn
            self.button = None

        self.is_active = is_active 

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)

class InputManager:
    def __init__(self):
        ''' A Manager for Keyboard Inputs '''
        self._pressed = []
        self._released = []
        self._held = []
        self._mouse_clicked = []
        self._mouse_released = []
        self._mouse_held = []
        self._mouse_motion = []
        
        self.mouse_position = pygame.mouse.get_pos()

    def bind_key_pressed(self, func, key=None, active=True):
        ''' Add a listener for when the key is pressed down. '''
        input_binding = InputBinding(key, func, InputType.KEY_PRESSED, is_active=active)
        self._pressed.append(input_binding)
        return input_binding

    def bind_key_release(self, func, key=None, active=True):
        ''' Add a listener for when the key is released. '''
        input_binding = InputBinding(key, func, InputType.KEY_RELEASED, is_active=active)
        self._released.append(input_binding)
        return input_binding

    def bind_key_held(self, func, key=None, active=True):
        ''' Add a listener for when the key is held down. '''
        input_binding = InputBinding(key, func, InputType.KEY_HELD, is_active=active)
        self._held.append(input_binding)
        return input_binding

    def bind_mouse_clicked(self, func, button=None, active=True):
        ''' 
        Add a listener for when the mouse specified button clicked. 
        Leave button as None for every mouse input.
        The callback given must accept event in its parameters.
        '''
        input_binding = InputBinding(button, func, InputType.MOUSE_CLICKED, mouse=True, is_active=active)
        self._mouse_clicked.append(input_binding)
        return input_binding

    def bind_mouse_released(self, func, button=None, active=True):
        '''
        Add a listener for when the mouse specified button released. 
        Leave button as None for every mouse input.
        The callback given must accept event in its parameters
        '''
        input_binding = InputBinding(button, func, InputType.MOUSE_RELEASED, mouse=True, is_active=active)
        self._mouse_released.append(input_binding)
        return input_binding

    def bind_mouse_held(self, func, button=None, active=True):
        ''' 
        Add a listener for when the specified mouse button is held down. 
        The callback given must accept mouse_x and mouse_y in its parameters
        '''
        input_binding = InputBinding(button, func, InputType.MOUSE_HELD, mouse=True, is_active=active)
        self._mouse_held.append(input_binding)
        return input_binding

    def bind_mouse_motion(self, func, active=True):
        ''' 
        Add a listener for when the mouse is moved. 
        The callback given must accept event in its parameters
        '''
        input_binding = InputBinding(None, func, InputType.MOUSE_MOTION, mouse=True, is_active=active)
        self._mouse_motion.append(input_binding)
        return input_binding
                
    def unbind_input(self, input, input_type:InputType):
        ''' Unbind a input of any kind from manager '''
        group = self._find_group(input_type)
        return self._unbind_input(group, input)

    @debug_and_log({
        'success':'Succussfully Cleared All Inputs',
        'error':'Inputs Clearing Error',
    })
    def clear_inputs(self):
        self._pressed.clear()
        self._released.clear()
        self._held.clear()
        self._mouse_clicked.clear()
        self._mouse_released.clear()
        self._mouse_held.clear()
        self._mouse_motion.clear()

    def activate_input(self, key, input_type:InputType):
        ''' Activate the input. This is done by change the specified inputs is_active to True '''
        group = self._find_group(input_type)
        for binding in group:
            if binding.key is not None:
                if binding.key == key:
                    binding.is_active = True

            else:
                if binding.button == key: 
                    binding.is_active = True

    def deactivate_input(self, key, input_type:InputType):
        ''' Deactivate the input. This is done by change the specified inputs is_active to False '''
        group = self._find_group(input_type)
        for binding in group:
            if binding.key is not None:
                if binding.key == key:
                    binding.is_active = False

            else:
                if binding.button == key: 
                    binding.is_active = False

    def _do_action_on_group(self, group, action, *args, **kwargs):
        for binding in group:
            action(binding, *args, **kwargs)

    def _remove_input(self, group, binding):
        group.remove(binding)
        del binding

    def _find_group(self, input_type:InputType) -> list:
        if input_type == InputType.KEY_PRESSED:
            return self._pressed
        elif input_type == InputType.KEY_RELEASED:
            return self._released
        elif input_type == InputType.KEY_HELD:
            return self._held
        elif input_type == InputType.MOUSE_CLICKED:
            return self._mouse_clicked
        elif input_type == InputType.MOUSE_RELEASED:
            return self._mouse_released
        elif input_type == InputType.MOUSE_HELD:
            return self._mouse_held
        elif input_type == InputType.MOUSE_MOTION:
            return self._mouse_motion

    def _unbind_input(self, bindings:list, input):
        for input_binding in bindings:
            if input_binding.key is not None:
                if input_binding.key == input:
                    self._remove_input(bindings, input_binding)
                    return input_binding

            else:
                if input_binding.button == input:
                    self._remove_input(bindings, input_binding)
                    return input_binding

    def _handle_mouse_click(self, event, bindings, mouse_btn_type):
        for input_binding in bindings:
            if input_binding.is_active:
                if event.type == mouse_btn_type:
                    if input_binding.any_input:
                        input_binding(event)

                    elif event.button == input_binding.button:
                        input_binding(event)

    def _handle_key_press(self, event, bindings, key_type):
        if event.type != key_type:
            return
    
        for input_binding in bindings:
            if not input_binding.is_active:
                continue
            
            if input_binding.any_input:
                input_binding()
    
            elif event.key == input_binding.key:
                input_binding()

    def update(self, events):
        keys = pygame.key.get_pressed()
        any_key_pressed = True in keys
        mouse_btns = pygame.mouse.get_pressed()
        self.mouse_position = pygame.mouse.get_pos()
        for event in events:
            for input_binding in self._mouse_motion:
                if input_binding.is_active:
                    if event.type == pygame.MOUSEMOTION:
                        input_binding(event)

            self._handle_mouse_click(event, self._mouse_clicked, pygame.MOUSEBUTTONDOWN)
            self._handle_mouse_click(event, self._mouse_released, pygame.MOUSEBUTTONUP)
            self._handle_key_press(event, self._pressed, pygame.KEYDOWN)
            self._handle_key_press(event, self._released, pygame.KEYUP)

        for input_binding in self._held:
            if not input_binding.is_active:
                continue
            
            if input_binding.any_input:
                if any_key_pressed:
                    input_binding()

            elif keys[input_binding.key]:
                input_binding()

        for input_binding in self._mouse_held:
            if input_binding.is_active:   
                x, y = self.mouse_position
                if input_binding.any_input:
                    input_binding(x, y)

                elif mouse_btns[input_binding.button - 1]:
                    input_binding(x, y)

