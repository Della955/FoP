def binarySearch(sorted_list, value):
    left = sorted_list[0] 
    right = sorted_list[len(sorted_list)-1] 
    

    for i in range (0, len(sorted_list)):
        mid = sorted_list[len(sorted_list) // 2]

        if mid == value:
            return mid 

        if value > mid:
            right = mid - 1
        
        if value < mid:
            left = mid + 1 
        
        if sorted_list[i] == value:
            return i

    return -1 
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 10)) 

print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 95)) # 16
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 100)) # -1