###Control flow
### Write a program that reads and integer and is checked against a set integer. 
### Then a message is displayed if inputted integer is same as the given integer
### Save program as if.py

number = 28
guess = int(input('Enter an integer: '))

if guess == number:
    print("Congratulations you have guessed the integer correctly", number)

elif guess<number:
    print("Sorry the number is little less")

else:
    print("Sorry the number if little high")

print('Done')
