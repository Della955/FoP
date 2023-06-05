


def hailstone(num):
    count = 0
    if num <= 0: 
        return "Please enter a positive number"
    if num == 1:
        return 0

    while (num != 1):
        if (num % 2 > 0):
            num = num * 3 + 1
        elif (num % 2 == 0):
            num = num / 2
        count += 1
    
    return count 

answer = hailstone(3)
print("Hailstone answer: ", answer)


    # if num is even, divide by 2 to get next int 
    # if nums is odd, multiply it y three and add one 



    
