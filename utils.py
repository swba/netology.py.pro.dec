from datetime import datetime
import os


def get_arg_string(*args, **kwargs) -> str:
    """Returns pretty-formatted string of arguments"""
    return ', '.join(
        list(map(str, args)) +
        list(f'{k}={v}' for k, v in kwargs.items()))

def log_func_call(path, func, *args, **kwargs):
    """Call a function, logs and returns the result"""
    if dirname := os.path.dirname(path):
        os.makedirs(dirname, exist_ok=True)
    with open(path, 'a', encoding='UTF-8') as file:
        res = func(*args, **kwargs)
        file.write("{}: {}({}) -> {}\n".format(
            f'{datetime.now():%d.%m.%Y %H:%M:%S}',
            func.__name__,
            get_arg_string(*args, **kwargs),
            str(res)
        ))
        return res
