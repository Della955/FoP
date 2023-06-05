def maxSubListSum(arr, num):
    #edge case check 
    #loop 
    #temp max
    end = len(arr) - num + 1
    if len(arr) < num:
        return None 
    
    temp_max = 0 

    for i in range(0, end):
        iteration_total = sum(arr[i:i+num])
        if iteration_total > temp_max:
            temp_max = iteration_total
    
    return temp_max 



    # for i in range(0, len(arr)-num+1):
    #     temp_max = 0
    #     for j in range(num):
    #         temp_max = temp_max[i+j]
    #         j+= 1
    #     totalArr.append(temp_max)
    #     i += 1
    # return max(totalArr)
    

    # return largest 
        
        
print(maxSubListSum([1, 2, 5, 2, 8, 1, 5], 2)) # 10
print(maxSubListSum([1, 2, 5, 2, 8, 1, 5], 4)) # 17
print(maxSubListSum([4, 2, 1, 6], 1)) # 6
print(maxSubListSum([4, 2, 1, 6, 2], 4)) # 13
print(maxSubListSum([], 4)) # None

        
