# 4. Reverse a String

def reverse_str(string):
    n = -1
    new_string = ''
    for l in string:
        new_string += string[n]
        n -= 1
    return new_string


print(reverse_str("1234abcd"))

# Sample Solution
# Define a function named 'string_reverse' that takes a string 'str1' as input
def string_reverse(str1):
    # Initialize an empty string 'rstr1' to store the reversed string
    rstr1 = ''
    
    # Calculate the length of the input string 'str1'
    index = len(str1)
    
    # Execute a while loop until 'index' becomes 0
    while index > 0:
        # Concatenate the character at index - 1 of 'str1' to 'rstr1'
        rstr1 += str1[index - 1]
        
        # Decrement the 'index' by 1 for the next iteration
        index = index - 1
    
    # Return the reversed string stored in 'rstr1'
    return rstr1