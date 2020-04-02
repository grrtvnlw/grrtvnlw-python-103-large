# given a number, print it's factors
# get user input for number and set total
inp = int(input("Give me a number, any number: ")) 
num = 1

# Logic
while num <= inp:
    if inp % num == 0: # if input can be divided evenly by number, it is a factor
        print(num)
        num += 1 # increment num by 1
        continue # start loop again
    else: # if input cannot be divided evenly by number, it is not a factor so we do not print
        num += 1 # increment num by 1
        continue # start loop again