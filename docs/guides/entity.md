# **Entities**
The **Entity** class is a class ment to be either as a ***super class*** or ***object***. It has many neat features that can come in handy during game development.

## Initialization
There are multiple ways to initialize an `Entity`.
You can either create an `Entity` with an image:
```python
entity = Entity(x, y, image)
```
Or you might want a rectangle:
```python
entity = Entity(x, y, size=(width, height), color=(Red, Green, Blue))
```
> **NOTE**: As of ***v0.1.6***, you do not need to load images with `pygame.image.load(filepath)`. You may use the `Asset Manager` within the `Game` class. For instance:

> `entity_image = game.assets.load_image('name', 'filepath')`

## Configurations
The `Entity` class have some handy features for different needs:

| Attribute | Description | Default |
|---|---|---|
| `x` | The x coordinate in the world. | — |
| `y` | The y coordinate in the world. | — |
| `image` | The image surface. | Optional |
| `size` | The size of the rectangle if no image is given. | Optional |
| `color` | The color of the rectangle if no image is given. Uses RGB. | White |
| `visible` | Whether the Entity should be drawn on the screen. | `True` |
| `paused` | Whether the Entity should be updated. | `False` |
| `active` | Whether the Entity should be drawn and updated. It prevents both updates and draw when false | `True` |
| `priority` | The priority of updates. Higher values have higher priority. | `0` |
| `layer` | The layer the Entity is drawn on, also known as the z-index. | `0` |
| `update_interval` | The interval at which the Entity is updated. | `UPDATE_EVERY_FRAME` |
| `tags` | The system used for sorting and group commands. | Empty set |
| `name` | The name displayed when the Entity is represented as a string. | `"Entity"` |
| `collision_group` | The group used for determining collision behavior. | `"None"` |
| `collision_mask` | The other Entity groups that this Entity can collide with. | Empty set |

***

[entity-api]:../api/entity.md
> For more on the API of Entities, read [here][entity-api]