def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("You can't use a negative number")
    elif type(n) != int:
        raise ValueError("Please enter an integer")
    else:
        return n * factorial(n-1)

print(factorial(5))