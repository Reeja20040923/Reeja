
import random

top_of_range = input("Type a number : ")

if top_of_range.isdigit():
  top_of_range = int(top_of_range)
  
  if top_of_range <= 0:
    print("Please enter the digit greater than zero next time")
    quit()
else:
  print("Please enter an integer next time")
  quit()



random_number = random.randint(0 ,top_of_range)
guesses = 0


while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
  
    else:
        print("Please enter an integer next time")
        continue
    if user_guess == random_number :
        print("you got it correct")
        break
    elif user_guess > random_number:
        print("You are gerater than the random number")
    else:
        print("you are less than the random number")
            
print("Hey you got it in",guesses,"guesses")


















