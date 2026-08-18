# **Scenes**
As of ***v0.1.7***, `Scene` and `SceneManager` were added into the engine. They allow you to create seperate and independent scenes. Just like in movie productions, where the film crew create seperate scenes to capture different events, `pygame-foundation` does the same. It allows you to create a series of events that are independent of each other. For instance, you want to make a RPG game where there is a a pause menu, a loading menu, and a game scene. Before you would have had to structure your code in such a way that it plays each of these accordingly. Basically, you would have to create the scene system from scratch. But now, that is redundant. 

> **NOTE**: Since the scene system is built into the game class, for all games you will need to create at least one scene. 

## Creation
The `Scene` class is ment to be used as a super class. It can be created extremely easily:
```py
from pygame_foundation.scene import Scene

class GameScene(Scene):
    def __init__(self, game, name):
        super().__init__(game, name)
```

## Methods
The Scene class has some methods that can come in handy.
```py
class GameScene(Scene):
    def __init__(self, game, name):
        super().__init__(game, name)

    def update(self, dt, events):
        ''' Overide this function for updates that take place every frame '''
        pass

    def draw(self, screen):
        ''' Overide this function for drawings and blits that take place every frame '''
        pass
```

As well as `update()` and `draw()`, Scene has `enter()`, `pause()` and more.

## Attributes
The `Scene` class has some neat attributes that are configurable to your need:
```py
class GameScene(Scene):
    def __init__(self, game, name):
        super().__init__(game, name)
        self.blocks_drawings = True
        self.blocks_updates = True


    def update(self, dt, events):
        ''' Overide this function for updates that take place every frame '''
        pass

    def draw(self, screen):
        ''' Overide this function for drawings and blits that take place every frame '''
        pass
```
The `Scene.blocks_drawings` and `Scene.blocks_updates` are attributes that take place when the scene is pushed. They affect the scene/s under the particular scene. `Scene.blocks_drawings` prevents underlaying scenes from drawing anything and `Scene.blocks_updates` prevents underlaying scenes from updating. They are defaulted to the following:
 
 - `Scene.blocks_drawings = False`
 - `Scene.blocks_updates = True`

## Manager
`pygame-foundation` comes with a `SceneManager`. It is to handle and manage the scenes. You may access it either by the `Game` class or manual creation:
```py
scene_manager = game.scene_manager
```
Or
```py
from pygame_foundation.scene import SceneManager

scene_manager = SceneManager(game)
```

### Changing the Scene
When creating a scene, you can change to it with the manager:
```py
game_scene = GameScene(game, 'GameScene')

scene_manager.change_scene(game_scene)
```

This will tell the manager that it should update and draw this scene.

### Overlaying Scenes
You may also overlay scenes, by using:
```py
game_scene = GameScene(game, 'GameScene')
game_scene2 = GameScene(game, 'GameScene2')

scene_manager.change_scene(game_scene)
scene_manager.push_scene(game_scene2)
```
This will overlay the pushed scene on top of the other scene. It can useful for scenes such as a transparent pause menu. You can also pop the top scene by using:

```py
scene_manager.pop_scene()
```

[scene-api]:../api/scenes/manager.md
> If you want to see all methods and the Scene Manager API, read [here][scene-api]

## Worlds
Since the addition of Scenes in ***v0.1.7***, World objects are not automatically created in the game class. You may add them in your scenes:
```py
from pygame_foundation.core import World

class GameScene(Scene):
    def __init__(self, game, name):
        super().__init__(game, name)
        self.world = World(game.camera)

    def update(self, dt, events):
        ''' Overide this function for updates that take place every frame '''
        self.world.update(dt)

    def draw(self, screen):
        ''' Overide this function for drawings and blits that take place every frame '''
        self.world.draw(screen)
```

This way you may also have multiple worlds, each independent of each other.

