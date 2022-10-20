import random
randomNumber=random.randint(1,50)

countGuess=0
userGuess=None

while userGuess != randomNumber:
    userGuess =int(input("Enter your guess num :"))
    countGuess = countGuess+1
    if userGuess == randomNumber:
        print("yes your guess is right")

    else:
        if userGuess < randomNumber:
            print("your guess is wrong , Enter a greter num")
    
        else:
                print("your guess is wrong , Enter a smaller num")
        
print("you have try " , countGuess , "times")