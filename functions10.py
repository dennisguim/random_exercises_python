# 10. Print Even Numbers from a Given List
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even(list):
    evens = [i for i in list if i % 2 == 0]
    return evens

print(even([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Sample solution

# Define a function named 'is_even_num' that takes a list 'l' as input and returns a list of even numbers
def is_even_num(l):
    # Create an empty list 'enum' to store even numbers
    enum = []
    
    # Iterate through each number 'n' in the input list 'l'
    for n in l:
        # Check if the number 'n' is even (divisible by 2 without a remainder)
        if n % 2 == 0:
            # If 'n' is even, append it to the 'enum' list
            enum.append(n)
    
    # Return the list 'enum' containing even numbers
    return enum

# Print the result of calling the 'is_even_num' function with a list of numbers
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9])) 