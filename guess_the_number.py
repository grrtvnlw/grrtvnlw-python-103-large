# build a guess the number game using user input and giving hints
# hard code the number 5 and save user input
winning_num = 5
inp = 0

# Logic
while inp != winning_num:
    print("I am thinking of a number between 1 and 10. ")
    inp = int(input("What's the number? "))
    if inp == winning_num:
        print("Yes! You win!")
        break # exit the loop
    elif inp < winning_num:
        print(str(inp) + " is too low.")
        continue # try again, go back to the while loop
    elif inp > winning_num:
        print(str(inp) + " is too high.")
        continue # try again, go back to the while loop