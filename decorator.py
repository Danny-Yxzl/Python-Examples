from functools import wraps
 
class decorator:
    def __init__(self):
        pass

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            print("You called the function.")
            return func(*args, **kwargs)
        return wrapped_function
 
@decorator()
def abc():
    print("Hello World!")


if __name__ == "__main__":
    abc()
