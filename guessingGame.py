import random
chances = 0
print("Number Guessing Game \n Guess a Number (between 1 and 9) : ")
rnumber = random.randint(1 , 9)
print(rnumber)
while chances < 5 :
    guess = int(input("Enter your guess : "))
    print(guess)
    if(guess == rnumber) :
        print("YOU WIN")
        break
    else :
        print("YOU LOSE")
    chances = chances + 1