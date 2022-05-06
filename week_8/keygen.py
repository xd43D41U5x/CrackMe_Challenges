import re

inputstring = """         (((((((param_1[17] == '1') && (*param_1 == 'A')) && (param_1[1] == 'C')) &&
            (((param_1[2] == 'T' && (param_1[8] == 'c')) &&
             ((param_1[3] == 'F' && ((param_1[13] == 'v' && (param_1[5] == 'N')))))))) &&
           ((param_1[6] == '0' &&
            (((param_1[11] == 'R' && (param_1[7] == '1')) && (param_1[15] == 'r')))))) &&
          (((param_1[9] == 'e' && (param_1[4] == '{')) &&
           (((param_1[10] == '_' && ((param_1[12] == '3' && (param_1[2] == 'T')))) &&
            (param_1[14] == '3')))))) &&
         ((((param_1[16] == '5' && (param_1[18] == '^')) && (param_1[19] == 'g')) &&
          (param_1[20] == '}'))))"""



cleaninput = inputstring.replace("(","").replace(")","")

inputlist = cleaninput.split("&&")

out = []

#Go through the expected string length
for x in range(21):
    #Go through each part of the list and pull out the correct string placement
    for i in inputlist:
        if re.findall(r"param_1\[(\d{0,2})",i):
            place = re.findall(r"param_1\[(\d{0,2})",i)[0]
        elif re.findall(r"\*param",i):
            place = "0"
        else:
            place = "na"
        #If the string place matches the loop count, append in order.
        if str(x) == place:
            actual = re.findall(r"\=\=\ ([^)]*)",i)[0]
            fixed = actual.replace("'","").replace(" ", "")
            out.append(fixed)
            break
            
    

print(" ".join(out))
