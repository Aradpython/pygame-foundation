# **Collisions**

`pygame-foundation` provides collision functionality through **collision groups** and **collision masks**. These properties allow Entities to define which other Entities they can collide with.

## Collision Groups

Every `Entity` can have a `collision_group`.

A collision group is the name used to identify the type of Entity for collision purposes.

For example:

```python
player = Entity(
    x=100,
    y=100,
    size=(50, 50),
    collision_group='player'
)
```

An enemy can have its own collision group:

```python
enemy = Entity(
    x=200,
    y=200,
    size=(50, 50),
    collision_group='enemy'
)
```

The default collision group is:

```python
"None"
```

## Collision Masks

An Entity can also have a `collision_mask`.

The collision mask determines which collision groups the Entity can collide with.

For example:

```python
player = Entity(
    x=100,
    y=100,
    size=(50, 50),
    collision_group='player',
    collision_mask={'enemy'}
)
```

In this example, the player belongs to the `player` collision group and can collide with Entities belonging to the `enemy` group.

## Collision Groups and Masks Together

Collision groups and masks are intended to work together.

For example, a simple game might contain:

```text
Player
    collision_group = "player"
    collision_mask  = {"enemy"}

Enemy
    collision_group = "enemy"
    collision_mask  = {"player"}

Wall
    collision_group = "wall"
```

This allows Entities to identify which types of Entities they are intended to interact with.

A complete example could look like:

```python
player = Entity(
    x=100,
    y=100,
    size=(50, 50),
    collision_group='player',
    collision_mask={'enemy', 'wall'}
)

enemy = Entity(
    x=300,
    y=100,
    size=(50, 50),
    collision_group='enemy',
    collision_mask={'player'}
)

wall = Entity(
    x=200,
    y=100,
    size=(50, 50),
    collision_group='wall',
    collision_mask={'player'}
)
```

## Configuring Collisions

The collision properties can be configured when creating an Entity.

They can also be changed later through the Entity's attributes:

```python
player.collision_group = 'player'
player.collision_mask = {'enemy'}
```

This can be useful when the collision behavior of an Entity needs to change during the game.

For example, an Entity could change its collision mask depending on its current state.

## Collision Groups vs Collision Masks

It is important to distinguish the two:

| Property | Purpose |
|---|---|
| `collision_group` | Defines what group the Entity belongs to |
| `collision_mask` | Defines which groups the Entity can collide with |

In other words:

```text
collision_group → "What am I?"

collision_mask → "What can I collide with?"
```

## API

For the complete collision-related API, see the **Entity API**.

[entity-api]: ../api/entity.md
> For more information on collision properties and the Entity API, read [here][entity-api]