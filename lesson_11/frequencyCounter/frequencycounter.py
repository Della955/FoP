def same(arr1, arr2):
    
    if len(arr1) != len(arr2):
        return False 
    
    num_dict = {} 

    for num in arr1:
        square = num**2 
        if square in num_dict:
            num_dict[square] += 1

        else:
            num_dict[square] = 1
    
    for num in arr2:
        if num in num_dict and num_dict[num] > 0:
            num_dict[num] -= 1
        else:
            return False  
    print(num_dict)
    return True 



print(same([1, 2, 3], [4, 1, 9])) # true
print(same([1, 2, 3], [1, 9])) # false
print(same([1, 2, 1], [4, 4, 1])) # false (must be same frequency)