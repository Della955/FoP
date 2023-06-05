def swap(int_list, index1, index2):
    int_list[index1], int_list[index2] = int_list[index2], int_list[index1]
    return int_list


def bubbleSortCount(arr):

    #sort list 
    comparisons = 0
    exchanges = 0 
    for i in range(len(arr)-1, -1, -1):
        for j in range(0, i):
            comparisons += 1 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                exchanges += 1 
    
    return comparisons, exchanges
        



    #keep track of comparisons 


print(bubbleSortCount([1, 2, 3, 5, 4, 6, 7])) # (21, 1)
print(bubbleSortCount([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # (45, 45)
print(bubbleSortCount([2, 1, 0, 5, 4])) # (10, 4)