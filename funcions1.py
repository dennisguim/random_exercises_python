# 1. Maximum of Three Numbers

def maximum(x, y, z):
    if x > y and x > z:
        return f'o valor máximo é {x}'
    if y > x > z:
        return f'o valor máximo é {y}'
    else:
        return f'o valor máximo é {z}'
    
print(maximum(1, 2, 3))

# Sample Solution

def max_of_two(x, y):
    # Check if x is greater than y
    if x > y:
        # If x is greater, return x
        return x
    # If y is greater or equal to x, return y
    return y

# Define a function that returns the maximum of three numbers
def max_of_three(x, y, z):
    # Call max_of_two function to find the maximum of y and z,
    # then compare it with x to find the overall maximum
    return max_of_two(x, max_of_two(y, z))


