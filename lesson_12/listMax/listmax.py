def list_max(arr_num, max_num=None, pos=0):
    
    if max_num == None:
        max_num = arr_num[0]

    if (len(arr_num) == 1):
        return arr_num[0]
    
    if pos == len(arr_num):
        return max_num

    if max_num < arr_num[pos]:
        max_num = arr_num[pos]
    
    return list_max(arr_num, max_num, pos+1)



print(list_max([-3, -8, -1000, -2, -3, -7, -88, -45]))
