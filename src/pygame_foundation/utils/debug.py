from functools import wraps
from termcolor import colored
from datetime import datetime

def debug_and_log(messages:dict, expected_errors=[Exception], end='\n'):
    ''' 
    A decorator that checks for errors and log the data to the terminal
    
    NOTE:
        Leave expected_errors as empty list to catch no errors
        and leave it as default to catch all errors
    '''
    if expected_errors is None:
        expected_errors = (Exception,)
    else:
        expected_errors = tuple(expected_errors)

    def get_error_message(error):
        error_messages = messages.get("errors", {})

        for error_type in type(error).__mro__:
            if error_type in error_messages:
                return error_messages[error_type]

        return messages["error"]

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # For instance methods, args[0] is normally `self`.
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            current_time = f"[{colored(timestamp, 'yellow')}]"

            try:
                result = func(*args, **kwargs)

            except expected_errors as error:
                message = colored(get_error_message(error), "red")
                print(f"{current_time}: {message}: {error}", end=end)
                return None

            success = colored(messages["success"], "green")
            print(f"{current_time}: {success}", end=end)

            return result

        return wrapper
    return decorator