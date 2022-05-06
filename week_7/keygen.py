import sys
import string
import random

def random_key():
    pool = string.ascii_letters + string.digits
    result = []
    for x in range(9):
        if (len(result)==4):
            result.append("-")
        else:
            result.append((random.choice(pool)))
    return result

def chartoint(value):
    value = []
    for v in valueinput:
        value.append(ord(v))
    return value


print("Choose option: ")
print("1. Enter your own key")
print("2. Generate Random key")
response = input(": ")
    
if (response == '1'):
    #Take user input as a string.
    maininput = input('Enter serial in format [abcd-1234]: ')
    if (len(maininput)!=9):
        print("Error: Input Serial must be 9 digits")
        sys.exit()
    valueinput = list(maininput)
    value = chartoint(valueinput)
elif (response == '2'):
    valueinput = random_key()
    value = chartoint(valueinput)
else:
    print("Not a valid number")
    sys.exit()

c1 = 0
output = 0

#Loop 100x performing conversion based on user serial input.
for x in range(100):
    res1 = ((value[0]+value[5]) ^ (value[2] | value[6])) & 0xF
    c1 += res1
    res2 = ((value[8] + (value[1] + value[7])) ^ c1) & 0xF0
    output+= res2

output2 = value[8] + output + value[3]

finaloutput = c1 + output + output2

inputprint = "".join(map(str,valueinput))
              
print("For the Serial: %s" % inputprint)
print("The resulting key is: %d" % finaloutput)
