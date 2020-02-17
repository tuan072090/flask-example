import time


def decorator_function(func):

    def wrapper(**kwargs):
        begin = time.time()

        num1 = kwargs.get("num1")
        print("num1 input is", num1)

        func(**kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return wrapper


@decorator_function
def calculate(num1=0, num2=0):
    total = num1 + num2

    print("total is ", total)
    return total


calculate(num1=3, num2=5)
