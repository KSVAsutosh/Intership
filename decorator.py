def greet():
    return "Good Morning User"

say_hello = greet
print(say_hello()) 
print("############################################")
#######################################################
def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def exclamation(func):
    def wrapper():
        result = func()
        return result + "!!!"
    return wrapper

@uppercase
@exclamation
def greet():
    return "hello"

print(greet())
print("############################################")
####################################################### 
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Done!")

slow_function()