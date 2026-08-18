# **Game Class**
The Game Class is class to store and update different aspects. It holds and updates every feature added.
It is built to only store all managers, update and run them.

## Initialization 
The game class can easily be created:
```python
game = Game(600, 400, "Caption", 60, (0, 0))
```

## Main Loop
To create and start a mainloop, you simply add the following line to your code:
```python
game.run()
```

[game-api]:../api/game.md
[scene-guide]:../guides/scenes.md

## Updates and Drawings
The game mainloop already takes care of this, hence there is no need to run `game.update()` and `game.draw()`.

> **NOTE**: The game class uses scenes in this current version. So you may need to create Scenes. For further information on Scenes and the Scene Manager and how to create one, look into _[here][scene-guide]_.

***

> For more on the `Game` API, read _[here][game-api]_.