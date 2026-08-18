# **Inputs**
As of version ***v0.1.2***, `Inputs` have been added into the engine. There are currently 2 forms of inputs with more to be added.

## Initialization
The `Game` class already creates a input manager. So you may access it by using `game.input_manager`. You may also initialize the class manually by using:
```python
from pygame_foundation.input import InputManager

input_manager = InputManager()
```

## Keyboard Inputs
In ***v0.1.2***, keyboard inputs were the first kind of inputs added. They can easily be created with `input_manager.bind_key_****(callback, key, active)`. The stars are there due to the fact that you can bind keys in three separate ways: 

 - Key Pressed: `input_manager.bind_key_pressed()`
 - Key Released: `input_manager.bind_key_released()`
 - Key Held: `input_manager.bind_key_held()`

> **NOTE**: Be reminded that the key must be a pygame key, such as `pygame.K_RIGHT`. As well as that, the active parameter is a boolean to determine whether the callback should be called during the activation of an input. The active parameter is defaulted to True.

## Mouse Inputs
As of ***v0.1.4***, Mouse inputs have been added. They work almost exactly like Keyboard inputs, with exception of having `bind_mouse_motion`.


## Input Contexts
As of ***v0.1.7***, with the addition of `Scenes`, you have to pass a context parameter to the bind methods. They are used to separate inputs bindings and preventing callbacks that are not part of the current scene. For example, if you have a pause menu and a game scene, when you are in the pause menu you cannot control the player. Because it is not part of the pause menu input context.


### Implementation
You may use the `.input_context` of the scene created. For instance: 
```python
game_scene = GameScene()

input_manager.bind_key_pressed(game_scene.input_context, callback, key, active)
```

or you can create your own input context by using:
```python
input_manager.create_context('Game Scene')
```

### Setting a Context
What I mean by setting, is setting the current input context. It can be done manually by using:
```python
game_context = input_manager.create_context('Game')

input_manager.set_context(game_context)
```

> **NOTE**: The `Scene Manager` will automatically set the input context when switching between scenes. 

[scene-guide]: ../guides/scenes.md
> For more on `Scenes`, read [here][scene-guide]

### Group Actions
You can do perform some actions on an input via its context:
```py
input_context.activate_input(key, input_type)
input_context.deactivate_input(key, input_type)

```


## Unbinding
Unbinding a key is extremely easy:
```python
input_manager.unbind_input(self, input_context, input_key, input_type):
```

## Input Types
To make it easier to read the code, I have added `InputType` which is an `Enum` subclass. What I mean by this is that you may use `InputType.KEY_PRESSED`, without having to create a Input Type object.

[inputs-api]: ../api/inputs/manager.md
> For more on the input system and it's API, read [here][inputs-api]