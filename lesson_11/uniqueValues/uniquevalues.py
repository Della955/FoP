def countUniqueValues(arr):
    if len(arr) == 0:
        return 0
    
    count = 1

    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            count += 1
    return count 


print(countUniqueValues([1, 1, 1, 1, 1, 2])) # 2
print(countUniqueValues([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13])) # 7
print(countUniqueValues([-2, -1, -1, 0, 1])) # 4
print(countUniqueValues([])) # 0