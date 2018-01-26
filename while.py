number = 23
running = True

while running:
    guess = int(input("Enter an integer: "))

    if guess == number:
        print("Conrgatulations you guessed the integer correctly")
        running = False
    elif guess<number:
        print("Sorry the number is little lesser")
    else:
        print("Sorry the number is little higher")
else:
    print("The while loop is over")

print ("Done")
