# **Timers**

`pygame-foundation` provides a timer system that can be used to execute callbacks after a specified amount of time or repeatedly at a specified interval.

The timer system consists of two classes:

- `Timer`: Represents an individual timer.
- `TimerManager`: Manages multiple timers and provides convenient methods for creating them.

## Timer Manager

The `Game` class provides access to the timer manager. You can use:

```python
game.timer_manager
```

The `TimerManager` can also be created manually:

```python
from pygame_foundation.core import TimerManager

timer_manager = TimerManager()
```

## Creating Timers

The easiest way to create a timer is through the `TimerManager`.

There are two main methods:

- `after()` — Run a callback after a specified amount of time.
- `every()` — Run a callback repeatedly at a specified interval.

### After

The `after()` method executes a callback after the specified amount of time.

```python
def say_hello():
    print("Hello!")

game.timer_manager.after(1000, say_hello)
```

The duration passed to `after()` is in **milliseconds**.

In this example, `say_hello()` will be called after 1000 milliseconds, which is 1 second.

You can also specify how many times the callback should run:

```python
game.timer_manager.after(1000, say_hello, loops=3)
```

This will execute the callback three times, once every second.

### Every

The `every()` method creates a timer that repeatedly executes a callback.

```python
def spawn_enemy():
    print("Enemy spawned!")

game.timer_manager.every(2000, spawn_enemy)
```

The callback will be executed every 2000 milliseconds (2 seconds).

An `every()` timer continues running until it is cancelled or removed.

## Timer Duration

There is an important difference between the `Timer` class and the `TimerManager` methods.

When creating a `Timer` directly, its duration is specified in **seconds**:

```python
timer = Timer(2, callback)
```

When using `TimerManager.after()` or `TimerManager.every()`, the duration is specified in **milliseconds**:

```python
game.timer_manager.after(2000, callback)
game.timer_manager.every(2000, callback)
```

Both examples represent a duration of 2 seconds.

> **NOTE**: `Timer` uses seconds, while `TimerManager.after()` and `TimerManager.every()` use milliseconds.

## Loops

Timers can be configured to execute their callback multiple times.

For example:

```python
game.timer_manager.after(1000, callback, loops=5)
```

The callback will execute once every second for a total of five executions.

The `loops` value must be at least `1`.

## Repeating Timers

A repeating timer can be created directly using the `Timer` class:

```python
timer = Timer(
    2,
    callback,
    repeat=True
)
```

When `repeat` is `True`, the timer continues executing its callback indefinitely until it is cancelled or removed.

The `TimerManager.every()` method is a convenient way of creating this type of timer:

```python
game.timer_manager.every(2000, callback)
```

## Cancelling a Timer

An individual `Timer` can be cancelled using:

```python
timer.cancel()
```

After being cancelled, the timer becomes inactive and will no longer execute its callback.

For example:

```python
timer = game.timer_manager.every(1000, callback)

timer.cancel()
```

## Adding Timers Manually

You may also create a `Timer` yourself and add it to the manager:

```python
from pygame_foundation.timer import Timer

timer = Timer(2, callback)

game.timer_manager.add(timer)
```

Multiple timers can be added at once:

```python
game.timer_manager.add(timer1, timer2, timer3)
```

When only one timer is passed to `add()`, that timer is returned. When multiple timers are passed, the timers are returned as a tuple.

## Removing Timers

A timer can be removed from the manager with:

```python
game.timer_manager.remove(timer)
```

Removing a timer prevents the manager from updating it.

You can also remove all timers:

```python
game.timer_manager.clear()
```

## Examples

### Delayed Callback

```python
def open_door():
    print("The door opened!")

game.timer_manager.after(3000, open_door)
```

The callback will run once after 3 seconds.

### Repeating Callback

```python
def spawn_enemy():
    print("Spawning enemy...")

game.timer_manager.every(5000, spawn_enemy)
```

The callback will run every 5 seconds.

### Repeating a Limited Number of Times

```python
def flash():
    print("Flash!")

game.timer_manager.after(500, flash, loops=4)
```

The callback will execute four times, with 500 milliseconds between each execution.

### Cancelling a Timer

```python
timer = game.timer_manager.every(1000, update_score)

# Later...
timer.cancel()
```

## API

For the complete list of methods and attributes, read the **Timer API** and **TimerManager API**.

[timer-api]:../api/timers/timer.md
> For more information on the `Timer` API, read [here][timer-api].

[timer-manager-api]:../api/timers/manager.md
> For more information on the `TimerManager` API, read [here][timer-manager-api].