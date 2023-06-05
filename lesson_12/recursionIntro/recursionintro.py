# def countdown(num):
#     result = ''
#     if num == 0:
#         return result.strip() 
    
#     result += str(num) + ' '
#     print(f'every iteration: {result}')
#     return result + countdown(num-1)
    
# print(countdown(10))

# def countup(num):
#     result = ''
#     if num == 0:
#         return result.strip()
#     result += str(num) + ' '
#     return countup(num-1) + result

# print(countup(10))

def sum_countup(num):
    count = 0 
    if num == 0:
        return count
    count = num + sum_countup(num-1)
    return count 

print(sum_countup(3))


