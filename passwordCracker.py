# importing random
from random import *

# taking input from user
password = input("Enter your password: ")

# storing alphabet letter to use thm to crack password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# initializing an empty string
allLetters = letters + numbers
guess = ""
guessesNum = 0
# target = 0
allLength = len(allLetters)
passColums = [0]

while(True):
    guess = ""
    for p in passColums:
        guess = allLetters[p] + guess
    # guess = allLetters[passColums[0]]
    guessesNum += 1
    print((guess))
    if guess == password:
        print("")
        print("password cracked! the password is: ", guess)
        print(guessesNum, "guesses used")
        break

    passColums[0] += 1
    if passColums[0] == allLength:
        for i in range(len(passColums)):
            if passColums[i] == allLength:
                passColums[i] = 0
                try:
                    passColums[i+1] += 1
                except IndexError:
                    passColums.append(0)




# while (guess != user_pass):
#     guess = ""
#     for letter in range(len(user_pass)):
#         guess_letter = password[randint(0, 25)]
#         guess = str(guess_letter) + str(guess)
#     print(guess)
    
# print("Your password is ", guess)