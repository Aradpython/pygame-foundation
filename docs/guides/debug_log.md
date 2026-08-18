# **Debugging**

`pygame-foundation` provides a `debug_and_log` decorator for handling errors and logging the result of function calls directly to the terminal.

The decorator can:

- Display a success message when a function completes successfully.
- Catch specified exceptions.
- Display a custom error message when an exception occurs.
- Display different messages for different exception types.
- Add a timestamp to each message.
- Display messages using terminal colors.

## Importing

The `debug_and_log` decorator is located in the `utils` package:

```python
from pygame_foundation.utils.debug import debug_and_log
```

## Basic Usage

The decorator is created by calling `debug_and_log()` and then applying it to a function.

For example:

```python
@debug_and_log({
    "success": "Function completed successfully!",
    "error": "Function failed!"
})
def my_function():
    print("Hello!")
```

When `my_function()` is called, the decorator will execute the function and print a timestamped success message if it completes successfully.

## Messages

The `messages` parameter is a dictionary containing the messages that should be displayed.

The general structure is:

```python
messages = {
    "success": "Success message",
    "error": "Error message"
}
```

### Success Messages

The `success` key is optional.

If it is provided and the decorated function completes successfully, the message will be printed:

```python
@debug_and_log({
    "success": "Player created!",
    "error": "Could not create player!"
})
def create_player():
    return Player()
```

If the `success` key is not provided, no success message is printed.

### Error Messages

The `error` key is used as the default error message when a caught exception occurs.

```python
@debug_and_log({
    "success": "Success!",
    "error": "Something went wrong!"
})
def divide(a, b):
    return a / b
```

If the function raises a caught exception, the decorator prints the error message together with the exception itself.

## Error-Specific Messages

Different exception types can have their own messages using the `errors` dictionary.

For example:

```python
@debug_and_log({
    "success": "Operation successful!",
    "error": "Operation failed!",
    "errors": {
        ValueError: "An invalid value was provided.",
        TypeError: "An invalid type was provided."
    }
})
def operation(value):
    ...
```

When an exception is raised, the decorator checks the exception's class hierarchy to find a matching message.

If a specific message is not found, the general `error` message is used.

## Expected Errors

The `expected_errors` parameter determines which exception types the decorator should catch.

By default:

```python
expected_errors=[Exception]
```

This means the decorator catches exceptions derived from `Exception`.

For example:

```python
@debug_and_log(
    {
        "success": "Success!",
        "error": "Something went wrong!"
    },
    expected_errors=[ValueError]
)
def convert_number(value):
    return int(value)
```

In this example, `ValueError` will be caught by the decorator.

Other exception types will not be caught by the decorator.

### Catching Multiple Exception Types

Multiple exception types can be provided:

```python
@debug_and_log(
    {
        "success": "Success!",
        "error": "Something went wrong!"
    },
    expected_errors=[ValueError, TypeError]
)
def operation(value):
    ...
```

### Catching All Errors

The default behavior catches exceptions derived from `Exception`:

```python
@debug_and_log(
    {
        "success": "Success!",
        "error": "Something went wrong!"
    }
)
def operation():
    ...
```

You can also explicitly use:

```python
expected_errors=None
```

which is treated as:

```python
(Exception,)
```

### Catching No Errors

To prevent the decorator from catching exceptions, pass an empty list:

```python
@debug_and_log(
    {
        "success": "Success!",
        "error": "Something went wrong!"
    },
    expected_errors=[]
)
def operation():
    ...
```

In this case, exceptions are not caught by the decorator and will propagate normally.

## Return Values

When the decorated function completes successfully, `debug_and_log` returns the function's original return value.

For example:

```python
@debug_and_log({
    "success": "Calculation completed!",
    "error": "Calculation failed!"
})
def calculate():
    return 10 + 20

result = calculate()

print(result)
```

`result` will contain:

```text
30
```

If a caught exception occurs, the decorator prints the error information and returns:

```python
None
```

## Timestamps

Every message printed by the decorator includes a timestamp.

The timestamp uses the following format:

```text
YYYY-MM-DD HH:MM:SS
```

For example:

```text
[2026-08-16 12:00:00]: Function completed successfully!
```

The timestamp is displayed in a different terminal color from the success and error messages.

## Custom Line Endings

The `end` parameter controls what is printed at the end of the log message.

By default:

```python
end='\n'
```

For example:

```python
@debug_and_log(
    {
        "success": "Success!",
        "error": "Error!"
    },
    end=""
)
def operation():
    ...
```

This can be useful when controlling how multiple log messages are displayed in the terminal.

## Complete Example

```python
from pygame_foundation.utils.debug import debug_and_log


@debug_and_log({
    "success": "Player loaded successfully!",
    "error": "Failed to load player!",
    "errors": {
        FileNotFoundError: "The player file could not be found.",
        ValueError: "The player data is invalid."
    }
})
def load_player(filepath):
    if filepath == "":
        raise ValueError("No filepath was provided.")

    with open(filepath, "r") as file:
        return file.read()


player = load_player("player.txt")
```

The decorator handles the logging and error messages while the function itself remains focused on loading the player.

## API

For the complete list of parameters and behavior, read the **Debug API**.

[debug-api]:../api/debug.md
> For more information on the `debug_and_log` API, read [here][debug-api].