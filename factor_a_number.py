# given a number, print it's factors
# get user input for number and set total
num = int(input("Give me a number, any number: "))
num_A = 1
num_B = num

while num > 0:
    if num_A * num_B == num:
        print(num_A)
        num_A += 1
        num_B -= 1
        num -= 1
        continue
    else:
        num_A += 1
        num_B -= 1
        num -= 1 
        continue 
    