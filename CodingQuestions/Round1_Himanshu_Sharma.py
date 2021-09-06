def balancedBrackets(expr):
    allowed = {"[": "]", "(": ")", "{": "}"}
    unbalanced = 0

    gotStartBracket = False

    for i in range(len(expr)-1):
        start = expr[i]

        if start in allowed:
            gotStartBracket = True
            
            if expr[i+1] != allowed[start]:
                unbalanced += 1
            else:
                unbalanced -= 1

    if gotStartBracket:
        if unbalanced:
            return "Not Balanced"
        else:
            return "Balanced"
    else:
        return "Not Balanced"

def findMissingNumber(seq):

    if seq != []:

        MIN = 1
        MAX = max(seq)
        
##        h = {i: True for i in seq}
##
##        for i in range(MIN, MAX+1):
##            try:
##                value = h[i]
##            except KeyError:
##                return i

        sumOfNNaturalNums = MAX*(MAX+1)/2.0
        sumOfseq = 0

        for i in seq:
            sumOfseq += i

        return sumOfNNaturalNums - sumOfseq

    else:
        return "Give a valid sequence"
    
            
        
