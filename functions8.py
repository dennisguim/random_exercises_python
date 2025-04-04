# 8. Return a New List with Distinct Elements from a List
# Sample List : [1,2,3,3,3,3,4,5]

def unique_list(list):
    uniq = set([nums for nums in list])
    list_uniq = [nums for nums in uniq]

    return list_uniq

print(unique_list([1,2,3,3,3,3,4,5]))

# Sample solution

# Define a function named 'unique_list' that takes a list 'l' as input and returns a list of unique elements
def unique_list(l):
    # Create an empty list 'x' to store unique elements
    x = []
    
    # Iterate through each element 'a' in the input list 'l'
    for a in l:
        # Check if the element 'a' is not already present in the list 'x'
        if a not in x:
            # If 'a' is not in 'x', add it to the list 'x'
            x.append(a)
    
    # Return the list 'x' containing unique elements
    return x

# Print the result of calling the 'unique_list' function with a list containing duplicate elements
print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))  