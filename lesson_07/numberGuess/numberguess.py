print("Enter the integer for the player to guess: ")
winning_number = int(input())

#print(f'The winning number you chose is: {winning_number}')

print('Enter your guess user: ')
user_guess = int(input())
guess_count = 1
if winning_number == user_guess: 
    print(f'You guessed it in 1 try, the correct answer was {winning_number}')
else:
    while user_guess != winning_number:
        if (user_guess > winning_number):
            print("Too high - try again:")
            user_guess = int(input())
            
        elif (user_guess < winning_number):
            print("Too low - try again:")
            user_guess = int(input())
        guess_count += 1
        
    
print(f"You guessed it in {guess_count} tries")
           
