#Important! This is a simple game for learning puposes. 

# Importing random library to enable to create random numbers
import random

#Interacting with the user
print("Hi. What is your name?")
name = input()
chat = "Nice to meet you {}. I am Charles_X and this is a simple guees number game. Enjoy it. :)"
print(chat.format(name))

count = 0
while True:
        count = count + 1
        try:
            number = int(input("What is your favorite number? "))
            break
        except ValueError:
            if count < 3:
                print (name + ", your favorite number must be a number, right?")
            else:
                print (name + ", stop trying to break the code")
while True:
        count = count + 1
        try:
            age = int(input("Ok. And how old are you? "))
            break
        except ValueError:
            if count < 3:
                print (name + ", your age must be a number, right?")
            else:
                print (name + ", stop trying to break the code")
print ("\nThank you!")
print("____________________________________________________________________________________________ \n")


#Logics behind random number
minNumber = 1
maxNumber = 100
magicNumber = random.randint(minNumber, maxNumber)

message = name + ", I'm thinking of a magic number. It's between {} and {}. Guess what it is. o/"
print(message.format(minNumber, maxNumber))

#Receiving input and handling exceptions
found = False
time = 0
errors = 0
while not found:
    time = time + 1
    while True:
        errors = errors + 1
        try:
            guess = int(input("Your guess: "))
            if (guess < minNumber) | (guess > 100):
                information = "     INFO: Remember between {} and {}!"
                print(information.format(minNumber, maxNumber))
            if guess == number:
                print ("Ha-Ha. So you tried your favorite number. Nice!")
            if guess == age:
                print ("Ah, obviously you would guess your age. :P")
            break
        except ValueError:
            if errors > 3:
                print ("What are you doing?? Let's play!")
            else:
                print (name + ", input must be a number, please reenter! ")    

#Comparing the magic number with user guess
    if guess == magicNumber:
        found = True
        print("____________________________________________________________________________________________ \n")
            
    if guess < magicNumber:
        if (magicNumber - guess > 10):
            print("No, no. Too low.")
        else:
            print("Low but getting closer.")
    if guess > magicNumber:
        if (guess - magicNumber > 10):
            print("Gee! Too high.")
        else:
            print("High but getting closer.")

#Counting how many times user guessed a number
    if time == 10:
        print("\n     Man, you have to finish this game. What is your problem?! \n")
    if time == 15:
        print("\n     Got it. You're having fun and don't want to finish the game. :D \n")
    if time == 20:
        print("\n     It's enough. You don't know how to play this game. Let's pretend you won. :S \n")
        break

#GameOver
print ("You got it! Congrats!!!")
print ("See you, " + name)
