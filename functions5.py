# 5. Factorial of a Number

def fatora(n):
    result = 1
    if n == 0:
        return 1
    else:
        while n > 0:
            result *= n
            n -= 1
        return result

print(fatora(0))


# Sample solution

# Define a function named 'factorial' that calculates the factorial of a number 'n'
def factorial(n):
    # Check if the number 'n' is 0
    if n == 0:
        # If 'n' is 0, return 1 (factorial of 0 is 1)
        return 1
    else:
        # If 'n' is not 0, recursively call the 'factorial' function with (n-1) and multiply it with 'n'
        return n * factorial(n - 1)

# Ask the user to input a number to compute its factorial and store it in variable 'n'
n = int(input("Input a number to compute the factorial: "))