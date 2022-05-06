import base64

#Get Filename
program=input('Enter the file name: ')

with open(program, 'r') as f:
    file=f.read()

#Functions to reverse the original encode. Convert from str > bytes > decode > return str
def b64decode(file):
    base64bytes = file.encode("utf-8")
    decodedBytes = base64.b64decode(base64bytes)
    decodedStr = decodedBytes.decode("utf-8")
    return decodedStr

def b32decode(file):
    base32bytes = file.encode("utf-8")
    decodedBytes = base64.b32decode(base32bytes)
    decodedStr = decodedBytes.decode("utf-8")
    return decodedStr

def b16decode(file):
    base16bytes = file.encode("utf-8")
    decodedBytes = base64.b16decode(base16bytes)
    decodedStr = decodedBytes.decode("utf-8")
    return decodedStr
    

encodedStr=file
count = 1

#As we have no way of knowing how many loops, we need to keep going until we no longer see the known/expected starting string.
while True:

    #Quick way to keep track of loops and the first few chars.  Just to make sure things are running right.
    print("Loop: %d - Start of current string is: %s" % (count, encodedStr[0:14]))

    #Strip everything but the encoded string we need.
    decodedStr = encodedStr.split("'",1)[1].split("'",1)[0]
    
    #Reverse the encoding.
    decodedStr=b16decode(decodedStr)
    decodedStr=b32decode(decodedStr)
    decodedStr=b64decode(decodedStr)

    #If the known starting string is no longer found, its been decoded and break.
    if "import base64;exec(base64.b64decode((base64.b32decode((base64.b16decode(" not in decodedStr:
        print("Decoded after %d loops.\n" % count)
        #Not really needed but lets print the final output nicely minus the 1k extra #'s.
        print(decodedStr.split("#"*1000)[0])
        break

    #Inc count and setup the decoded string to the encoded for another round.
    count += 1
    encodedStr = decodedStr
