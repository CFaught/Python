#factorial.py
#Author: Caleb Faught
# this is a simple example of recursion that
# calculates the factorial of a positive integer.

def factorial(n):
    #this is basically our end case where the recursion stops
    #unless the original number entered is <= 1..
    if n <= 1:
        return 1
    # this is the recursive part that cycles through the 
    # function until n = 1.
    else:
        r = n * factorial(n - 1)
        return r
#call the function with an input as the argument..
num = int(raw_input('Enter a non-negative integer: '))
print 'the factorial of %d is ' % num + str(factorial(num))
