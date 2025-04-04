# 10. Print Even Numbers from a Given List
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even(list):
    evens = [i for i in list if i % 2 == 0]
    return evens

print(even([1, 2, 3, 4, 5, 6, 7, 8, 9]))