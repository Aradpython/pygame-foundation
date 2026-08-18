# **Camera**
As of ***v0.1.5***, the `Camera` class has been added. It can be extremely useful in most games.

## Initialization
The `Camera` class is automatically initiated in the `Game` class. So you may use `Game.camera` or initiate it manualy via `Camera(position, window_width, window_height)`.

## Position
The camera class turns the world coordinates into screen coordinates. You may change the location of a rectangle from world to screen coordinates via `camera.apply(rect)`.

## Movement
There are two ways of moving the camera:

### Manual
You can manualy move the camera with `camera.move(dx, dy)`. The `dx` and `dy` are distance to be moved, **not** coordinates to be moved to.

### Following
You may also make the camera follow a rectangle via `camera.follow(rect)`. 
And if later you want to make the camera stop following the rectangle, you can use `camera.stop_following()`.


[here]: ../api/camera.md
> For more on the Camera API, read [here].