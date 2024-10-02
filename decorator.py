import functools

## This is a template for a decorator
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something...
        res = func(*args, **kwargs)
        # Do something...
        return res
    return wrapper

@start_end_decorator
def add_5(x):
    return x+5

result = add_5(10)
print(result)

print(help(add_5))
print(add_5.__name__)

def repeat(num_times):
    def decorator_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                r = func(*args, **kwargs)
            return r
        return wrapper
    return decorator_func

@repeat(num_times=3)
def greet(name):
    print(f'hello {name}')

greet('Anshuman')