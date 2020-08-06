def checkPalindrome(inputString):
    for i in range(0, len(inputString)):
        if inputString[i] == inputString[(len(inputString)-i)-1]:
            continue
        else: 
            return False
    return True

##Basically when you define your function input, it is a placeholder for the actual input value; in this case inputString can be anything you pass to the function.We begin by defining our single for loop to start at index 0 and go up to the length of the input string - 1. Within the loop we compare the first character to the last character, in other words:

##Basically, so long as we don't find two values that don't match we continue until the end and return true, else the moment we find two values or characters that don't match, we return false.
