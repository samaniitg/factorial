
""" helper functions """

def factorial(n):
    """ function to return factorial of a number """
    return 1 if (n==1 or n==0) else n * factorial(n - 1)