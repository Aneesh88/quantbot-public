from datetime import datetime
import traceback
from error_log_utils import log_error

def format_time():
    """Return current time formatted as YYYY-MM-DD HH:MM:SS."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def try_or_log(default=None):
    """
    Decorator to wrap a function and log exceptions using log_error.
    Returns default value if an exception occurs.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                log_error(f"[utils] Error in {func.__name__}:\n{traceback.format_exc()}")
                return default
        return wrapper
    return decorator
