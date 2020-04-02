# given a number, print it's factors
# get user input for number and set total
inp = int(input("Give me a number, any number: ")) / 2 # to reduce loops
num = 1


while num <= inp:
    if inp % num == 0:
        print(num)
        num += 1
        continue

    