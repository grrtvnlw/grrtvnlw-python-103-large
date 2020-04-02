# given a number, print it's factors
# get user input for number and set a variable for factor numbers
inp = int(input("Give me a number, any number: ")) 
num_of_factor = 1

# Logic
while num_of_factor <= inp:
    if inp % num_of_factor == 0: # if input can be divided evenly by number, it is a factor
        print(num_of_factor)
        num_of_factor += 1 # increment factor by 1
        continue # start loop again
    else: # if input cannot be divided evenly by number, it is not a factor so we do not print
        num_of_factor += 1 # increment factor by 1
        continue # start loop again