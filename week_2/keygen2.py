import random
import string

first = ""

#Create first set of 4 digits, anything between 0-9.
for x in range(0,4):
    random1 = random.randint(0,9)
    first = first + str(random1)

Final = first + "-"

second = ""

#Create second set of 4 digits, even numbers only.
for x in range(0,4):
    while len(second) < 4:
        random2 = random.randint(0,9)
        if (random2 % 2) == 0:
            second = second + str(random2)

Final = Final + second + "-R"

#Create third set of 4 digits(char), "R" is constant, the other 3 random letters and digits.
third = "".join(random.choices(string.digits+string.ascii_letters,k=3))

Final = Final + third

print("Key Generated:")
print(Final)

