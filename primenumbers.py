import math

num = int(input("Enter a number: "))
factors = []

if num > 1:
    for a in range(1, num+1):
        quotient = num / a
        remainder = num % a
        factor = math.floor(quotient)
        if remainder == 0:
            factors.append(factor)

    if len(factors) == 2:
        print(str(num) + " is a prime number.")
        print("Proof: ")
        print("Since " + str(num) + " has only " + str(len(factors)) + " factors " + str(factors) + ", it is a prime number.")
    else:
        print(str(num) + " is a composite number.")
        print("Proof: ")
        print("Since " + str(num) + " has " + str(len(factors)) + " factor " + str(factors) + ", it is a composite number.")
else:
    print(str(num) + " is neither prime nor composite.")
