def is_decreasing(arr_list, pos=1, is_smaller=True):
    
    if pos == len(arr_list)-1:
        return is_smaller
    
    if arr_list[pos] > arr_list[pos+1]:
        is_smaller = True 
    else:
        is_smaller = False 
    
    return is_decreasing(arr_list, pos+1, is_smaller) 


print(is_decreasing([5,4,3,2,1]))
print(is_decreasing([1,2,3,4,5]))
print(is_decreasing([5,4,3,2,1,8]))