roll_again = input("Would you like to fish again? \"y\" for yes or \"n\" for no: ")

if roll_again == "yes" or roll_again == "y":
    while roll_again =="yes" or roll_again =="y":
        print("Casting your line...")
        time.sleep(1)
        print("...Waiting for a bite...")
        time.sleep(3)
        print("You have caught a...")
        time.sleep(1)
        print(dice_roll)
elif roll_again == "no" or roll_again == "n":
    print("Okay. Thanks for playing")
    exit()
else:
    print("I'm sorry, please type either \"y\" for yes or \"n\" for no")