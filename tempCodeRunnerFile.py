# 8. Return a New List with Distinct Elements from a List
# Sample List : [1,2,3,3,3,3,4,5]

def unique_list(list):
    list_uniq = [nums if nums not in list_uniq else continue 
                 for nums in list
                 ]
    return list_uniq

print(unique_list([1,2,3,3,3,3,4,5]))