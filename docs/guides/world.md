# **Worlds**
The **World** class acts as a sprite group for all **Entities**. It has multiple useful features as stated below:

## Initialization
```
world = World(game.camera)
```

[scene-guide]:scenes.md

> **WARNING**: As of __v0.1.7__, the world class is not automatically created in the Game class. You may create them in your scenes. For further information on Scenes and how to create and implement Worlds into Scenes, read _[here][scene-guide]_.


## Sprites/Entities
The world class is a improved version of pygame Groups. When adding _sprites/entities_ into the world, the class automatically sorts them by **priorities**, **layers**, and **tags**.

An example of how you can add _sprites/entities_:
```python
world.add(sprite1, sprite2)
```

Behind the scenes, the world class will look for the properties in an Entity, and by sorting them, it enables priority updates and layered drawing. As well as tag updates, such as `pause_tag()` and `resume_tag()`. 

## Updates
The world class will automatically update an Entity. You also have some neat features for update intervals and update priorities.

### Update Intervals
When creating an Entity, you can specify the update interval. You may also change the priority later using  `entity.update_interval`. It is normaly set to `UPDATE_EVERY_FRAME`, which is self-explanatory. 

By using the delta time from `clock.tick(fps)`, it updates entities at an interval.


### Update Priorities
When creating an Entity, you can specify the update priority. You may also change the priority later using  `entity.priority`. The default is 0. The higher it is set the higher priority it is.

By sorting the entities by their priority, the world class updates the entities.


## Drawing
The world class has a layering system, which works almost exactly like the update priorities.
You can set the `layer` when creating an Entity or later on.

## Tags
Most games using **OOP** use multiple sprite groups, but the world class is only one group. To solve that problem I have added `tags`. By using tags you can seperate entities into sprite-group-like lists, which you can perform actions on. 
For example:
```python
world.activate_tags('enemies')
enemies = world.find_by_tags('enemies')
```

> **Pausing**: You can also **pause** tags which will prevent updating the entity. As well as **hide** tags which will prevent drawing the entity. Or prevent both by **deactivating** tags. All of these actions can be reversed as well, for example show tags or resume tags.

***

[entity-guide]:../guides/entity.md
> For more on Entities, read [here][entity-guide]

[world-api]:../api/world.md
> For more on the World API, read [here][world-api]

[entity-api]:../api/entity.md
> For more on the Entity API, read [here][entity-api]

