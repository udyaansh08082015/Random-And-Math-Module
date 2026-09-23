import random
playing = True
number = str(random.randint(0,100))

print("I will generate a number from 0-100,will you be able to guess it?")

while playing:
    guess=input("Give me your best guess!\n")
    if number==guess:
        print("Great Job! You guessed the number!")
        print("The number was",number)
        break
    else:
        print("Try Again!")



    




