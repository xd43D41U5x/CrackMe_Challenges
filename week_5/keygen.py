def shiftletters(letter, n):
    return chr((ord(letter) - 97 + n % 26) % 26 + 97)

userName = input("Enter the UserName: ")
number = input("Enter the number: ")
number = int(number)+7
result = ""
for u in userName:
    shift = shiftletters(u,number)
    result += shift

print(result)
