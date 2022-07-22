fullClintStr = input("please enter text: ")
strlen = len(fullClintStr)
lowerCaseStr = fullClintStr.lower()
upperCaseStr = fullClintStr.upper()
cutlen = strlen - (strlen//2)
printStr = lowerCaseStr[:cutlen] + upperCaseStr[cutlen:]
print(printStr)
input("yes")