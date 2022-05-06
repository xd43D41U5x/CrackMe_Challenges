import random

def keygen():
    key_list = []
    while True:
        #Try to get a good mix of short and long numbers for variety.
        mix = random.randint(1,100)
        if mix % 2 == 0:
            n = random.randint(100,1000)
        else:
            n = random.randint(100000,900000)
            
        isPrime = True

        #Check to see if any other number will divide evenly.
        for num in range(2, n):
            if n % num == 0:
                isPrime = False
                break

        #Check to see if its prime and length modulo 3 equals 0.        
        if isPrime and (len(str(n)) % 3 == 0):
            key_list.append(n)

        #Just generate 10 of these.
        if len(key_list) == 10:
            break
    return key_list

key_list = keygen()

print('Generated Keys (10): ')

for p in key_list:
    print(p)
