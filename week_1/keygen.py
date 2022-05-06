#There is much more code here than needed but I wanted to show the output from each step for learning.

#Initial Length to test
x = 9

#Perform bitwise NOT on length 9
notout = hex(int((bin(~x & 0xffffffff)),2))

print("After a bitwise NOT, the initial length is stored as: %s" % notout)

#Convert the hex value to int and add one
num1 = int(notout,16) + 1

print("We increment that value and get %s" % hex(num1))

#Convert 60h to an int and add
addsixty = num1 + int('0x60',16)

hexnum = hex(addsixty)[-8:]

print("We add 60h to that value and get: %s" % hexnum)

#Example first character
firstchar = int('0x27',16)

#Bitwise Xor the int of the first character and the hexnumber.
xornum = int(hexnum,16) ^ firstchar

print("For example we xor that with the expected pw and get the ascii char: %s" % chr(xornum))
print("Lets go through the entire pw now!\n")

plainpw = "'/+=)8iig"
cipher = ""
strlen = len(plainpw)
count = 0

starthex = num1

#Loop through the entire string one char at a time
while count < strlen:
    c = plainpw[count]
    #Convert ascii intput to an int number
    intc = ord(c)
    #Bitwise Xor that int value with the known hex value.
    xornum = (int(hexnum,16) + count) ^ intc
    print("Input %s converts to %s" % (c,chr(xornum)))
    #Build the output string.
    cipher += chr(xornum)
    #Increment char count and go to the next
    count += 1

#Output final cipher string pw
print("\nFinal cipher string is: %s" % cipher)
