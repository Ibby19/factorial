def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("You can't use a negative number")
    elif type(n) != int:
        raise ValueError("Please enter an integer") #you need to put this earlier, else you will get a TypeError when checking n<0
    else:
        return n * factorial(n-1)

print(factorial(5))

#better: take input from user
