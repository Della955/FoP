def multiply(num1, num2):
    total = 0 
    if num2 == 1:
        total += (num1 * num2)
        return total 
    total += num1 
    return multiply(num1, num2-1) + total 


print(multiply(7,4))
    

