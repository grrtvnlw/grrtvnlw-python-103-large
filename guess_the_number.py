# build a guess the number game using user input and giving hints
# import randint function from random module
from random import randint
# set game counter variable, will decrement so guesses left works
counter = 5
# make the winning number a random integer 
winning_num = randint(1, 10)

# Logic
while counter >= 0:
    if counter != 0: # if user still has guesses left
        # prompt the user for input
        print(f"I am thinking of a number between 1 and 10. \nYou have {counter} guesses left.")
        # update the input variable to hold user input
        inp = int(input("What's the number? "))
        if inp == winning_num: 
            print("Yes! You win!")
            play_again = input("Do you want to play again (Y or N)? ")
            if play_again == "Y":
                counter = 5 # reset counter to 5 
                # have to reset winning number or else it will be the same as last game
                winning_num = randint(1, 10)
                continue
            elif play_again == "N":
                print("Bye!")
                break # exit the loop
        elif inp < winning_num:
            print(str(inp) + " is too low.") # f-string wouldn't work here
            counter -= 1 
            continue # try again, go back to the while loop
        elif inp > winning_num:
            print(str(inp) + " is too high.") # f-string wouldn't work here
            counter -= 1 
            continue # try again, go back to the while loop
    elif counter == 0: # if user has run out of guesses
        play_again = input("You lose. Do you want to play again (Y or N)? ")
        if play_again == "Y":
            counter = 5 # reset counter to 5 
            # have to reset winning number or else it will be the same as last game
            winning_num = randint(1, 10)
            continue
        elif play_again == "N":
            print("Bye!")
            break
            