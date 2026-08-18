# **Assets**

The **Asset Manager** is used to load and manage assets used throughout your game. It is provided by the `Game` class, allowing you to load assets without having to manually load and manage them throughout your project.

## Accessing the Asset Manager

The `Game` class automatically creates an Asset Manager. You may access it through:

```python
game.assets
```

For example:

```python
entity_image = game.assets.load_image('player', 'assets/player.png')
```

The loaded image can then be passed to an `Entity`:

```python
player = Entity(
    x=100,
    y=100,
    image=entity_image
)
```

> **NOTE**: As of ***v0.1.6***, you do not need to manually load images using `pygame.image.load()`. The Asset Manager can be used to load and manage your images instead.

## Loading Images

Images can be loaded using `load_image()`:

```python
entity_image = game.assets.load_image('player', 'assets/player.png')
```

The first parameter is the name used to identify the asset, while the second parameter is the path to the image.

The returned image is a `pygame.Surface`, which can be used anywhere a normal pygame image surface would be used.

For example:

```python
player_image = game.assets.load_image(
    'player',
    'assets/player.png'
)

player = Entity(
    x=100,
    y=100,
    image=player_image
)
```

## Asset Names

Assets are given names when they are loaded. This allows the Asset Manager to identify them separately.

For example:

```python
game.assets.load_image('player', 'assets/player.png')
game.assets.load_image('enemy', 'assets/enemy.png')
```

The two images can therefore be managed as separate assets:

```text
player → player.png
enemy  → enemy.png
```

This can be useful when your game contains many assets and you want to keep them organized through the Asset Manager.

## Using Assets with Entities

One of the main uses of the Asset Manager is loading images that will be used by Entities.

For example:

```python
player_image = game.assets.load_image(
    'player',
    'assets/player.png'
)

player = Entity(
    x=100,
    y=100,
    image=player_image
)
```

This keeps asset loading separate from the Entity itself.

Instead of having an Entity responsible for finding and loading an image file, the Asset Manager handles the asset and the Entity receives the resulting image.

## Asset Manager and Game

Because the Asset Manager is created by the `Game` class, it is normally accessed through the game instance:

```python
game.assets
```

This means that different parts of your game can use the same Asset Manager instead of creating separate managers for every Entity or Scene.

## API

For the complete list of methods and attributes provided by the Asset Manager, read the **Asset Manager API**.

[assets-api]:../api/assets/manager.md
> For more information on the Asset Manager API, read [here][assets-api]