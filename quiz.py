# online quiz

name=input("Please enter your name :")
print(f"Hello {name} !!! Welcome to the computer quiz")
quiz=input("Are you ready to start the quiz now ?")

if quiz.lower() != "yes":
    quit()
else:
    print("You're time starts now")
score=0


print("Here is your 1st question:")
answer=input("1.Who is the Prime Minister of India ? ")
if answer.lower() == "narendra modi" :
    print("You are absolutely correct ! ")
    score += 1
else :
    print("Oops! try next question")

print("Here is your 2nd question:")
answer=input("2.Who is called as Nightangle of India ")
if answer.lower() == "sarojini naidu" :
    print("You are absolutely correct ! ")
    score += 1
else :
    print("Oops! try next question")
    


print("Here is your 3rd question:")
c=int(input("3.How many states are present in India ? "))
if c==29 :
    print("You are absolutely correct ! ")
    score += 1
else :
    print("Oops! thats the end for now")
    
print(f"{name} you have answered {score} number of questions ")
print(f"Your final score is {score/3*100} %. ")


print("Thats all for now.... see you later ")


    
    
    
