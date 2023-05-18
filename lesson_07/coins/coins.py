num = int(input("Please enter an amount in cents less than a dollar:\n"))

quarters = num // 25
num = num % 25
dimes = num // 10
num = num % 10
nickels = num // 5 
num = num % 5
penny = num // 1
num = num % 1
print("Quarters: ", quarters, "\nDimes: ", dimes, "\nNickels: ", nickels, "\nPenny: ", penny)
