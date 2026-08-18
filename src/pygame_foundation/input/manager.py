from pygame_foundation.utils.debug import debug_and_log
from enum import Enum
import pygame

class InputType(Enum):
    ''' A Enum subclass used to store input types. '''
    KEY_PRESSED = 1
    KEY_RELEASED = 2
    KEY_HELD = 3
    MOUSE_CLICKED = 4
    MOUSE_RELEASED = 5
    MOUSE_HELD = 6
    MOUSE_MOTION = 7

class InputBinding:
    ''' A class used to store metadata for input bindings '''
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

class InputContext:
    ''' A class used to store input bindings and separate them. Used in Scenes for making paused inputs. '''
    def __init__(self, name):
        self.name = name
        self._key_pressed = []
        self._key_released = []
        self._key_held = []
        self._mouse_clicked = []
        self._mouse_released = []
        self._mouse_held = []
        self._mouse_motion = []

    @debug_and_log({
        'success':'Succussfully Cleared All Inputs',
        'error':'Inputs Clearing Error',
    })
    def clear_inputs(self):
        ''' Clears all inputs from the context. '''
        self._key_pressed.clear()
        self._key_released.clear()
        self._key_held.clear()
        self._mouse_clicked.clear()
        self._mouse_released.clear()
        self._mouse_held.clear()
        self._mouse_motion.clear()

    def activate_input(self, key, input_type:InputType):
        ''' Activates the input. This is done by change the specified inputs is_active to True '''
        group = self._find_group(input_type)
        for binding in group:
            if binding.key is not None:
                if binding.key == key:
                    binding.is_active = True

            else:
                if binding.button == key: 
                    binding.is_active = True

    def deactivate_input(self, key, input_type:InputType):
        ''' Deactivates the input. This is done by change the specified inputs is_active to False '''
        group = self._find_group(input_type)
        for binding in group:
            if binding.key is not None:
                if binding.key == key:
                    binding.is_active = False

            else:
                if binding.button == key: 
                    binding.is_active = False

    def _find_group(self, input_type:InputType) -> list:
        if input_type == InputType.KEY_PRESSED:
            return self._key_pressed
        elif input_type == InputType.KEY_RELEASED:
            return self._key_released
        elif input_type == InputType.KEY_HELD:
            return self._key_held
        elif input_type == InputType.MOUSE_CLICKED:
            return self._mouse_clicked
        elif input_type == InputType.MOUSE_RELEASED:
            return self._mouse_released
        elif input_type == InputType.MOUSE_HELD:
            return self._mouse_held
        elif input_type == InputType.MOUSE_MOTION:
            return self._mouse_motion

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
        ''' Updates the Input Context object '''
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
            self._handle_key_press(event, self._key_pressed, pygame.KEYDOWN)
            self._handle_key_press(event, self._key_released, pygame.KEYUP)

        for input_binding in self._key_held:
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

class InputManager:
    ''' A class for managing Inputs and Input Contexts. '''
    def __init__(self):
        ''' A Manager for Keyboard Inputs '''
        self.contexts = []
        self.current_context = None

        self.mouse_position = pygame.mouse.get_pos()

    def create_context(self, name) -> InputContext:
        ''' Creates and binds a Context object. '''
        context = InputContext(name)
        self.contexts.append(context)
        return context

    def set_context(self, input_context:InputContext):
        ''' Sets the current Input Context. '''
        if input_context not in self.contexts:
            raise ValueError(f"Context '{input_context.name}' is not registered")

        self.current_context = input_context

    def bind_key_pressed(self, context:InputContext, func, key=None, active=True):
        ''' Add a listener for when the key is pressed down. '''
        if context not in self.contexts:
            raise ValueError(
                f"Context '{context.name}' is not known by the Input Manager"
            )
        return self._bind_key(context, key, func, InputType.KEY_PRESSED, active, context._key_pressed)

    def bind_key_release(self, context:InputContext, func, key=None, active=True):
        ''' Add a listener for when the key is released. '''
        if context not in self.contexts:
            raise ValueError(
                f"Context '{context.name}' is not known by the Input Manager"
            )
        return self._bind_key(context, key, func, InputType.KEY_RELEASED, active, context._key_released)

    def bind_key_held(self, context:InputContext, func, key=None, active=True):
        ''' Add a listener for when the key is held down. '''
        if context not in self.contexts:
            raise ValueError(
                f"Context '{context.name}' is not known by the Input Manager"
            )
        return self._bind_key(context, key, func, InputType.KEY_HELD, active, context._key_held)

    def bind_mouse_clicked(self, context:InputContext, func, button=None, active=True):
        ''' 
        Add a listener for when the mouse specified button clicked. 
        Leave button as None for every mouse input.
        The callback given must accept event in its parameters.
        '''
        if context not in self.contexts:
            raise ValueError(
                f"Context '{context.name}' is not known by the Input Manager"
            )
        return self._bind_key(context, button, func, InputType.MOUSE_CLICKED, active, context._mouse_clicked, mouse=True)

    def bind_mouse_released(self, context:InputContext, func, button=None, active=True):
        '''
        Add a listener for when the mouse specified button released. 
        Leave button as None for every mouse input.
        The callback given must accept event in its parameters
        '''
        if context not in self.contexts:
            raise ValueError(
                f"Context '{context.name}' is not known by the Input Manager"
            )
        return self._bind_key(context, button, func, InputType.MOUSE_RELEASED, active, context._mouse_released, mouse=True)

    def bind_mouse_held(self, context:InputContext, func, button=None, active=True):
        ''' 
        Add a listener for when the specified mouse button is held down. 
        The callback given must accept mouse_x and mouse_y in its parameters
        '''
        if context not in self.contexts:
            raise ValueError(
                f"Context '{context.name}' is not known by the Input Manager"
            )
        return self._bind_key(context, button, func, InputType.MOUSE_HELD, active, context._mouse_held, mouse=True)
    
    def bind_mouse_motion(self, context:InputContext, func, active=True):
        ''' 
        Add a listener for when the mouse is moved. 
        The callback given must accept event in its parameters
        '''
        if context not in self.contexts:
            raise ValueError(
                f"Context '{context.name}' is not known by the Input Manager"
            )
        return self._bind_key(context, None, func, InputType.MOUSE_MOTION, active, context._mouse_motion, mouse=True)

    def _bind_key(self, context:InputContext, key, func, input_type, is_active, group, mouse=False):
        if context not in self.contexts:
            raise ValueError(
                f"The context '{context.name}' is not known by the Input Manager"
            )

        input_binding = InputBinding(
            key,
            func,
            input_type,
            is_active=is_active,
            mouse=mouse
        )

        group.append(input_binding)
        return input_binding

    def _do_action_on_group(self, group, action, *args, **kwargs):
        for binding in group:
            action(binding, *args, **kwargs)

    def _remove_input(self, group, binding):
        group.remove(binding)
        del binding

    def update(self, events):
        ''' Updates the current Input Context '''
        if self.current_context is not None:
            self.current_context.update(events)
        
    def unbind_input(self, context:InputContext, input, input_type:InputType):
        ''' Unbind a input of any kind from the Input Context. '''
        if context not in self.contexts:
            raise ValueError(
                f"Context '{context.name}' is not known by the Input Manager"
            )
        group = context._find_group(input_type)
        return self._unbind_input(group, input)

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



