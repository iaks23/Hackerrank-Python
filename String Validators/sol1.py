if __name__ == '__main__':
    s = input()
    alnumcheck = False
    alphacheck = False
    numcheck = False
    lowcheck = False
    upcheck = False
    
    for char in s:
        if char.isalnum():
            alnumcheck = True
    print(alnumcheck)
    
    for char in s:
        if char.isalpha():
            alphacheck = True 
    print(alphacheck)
    
    for char in s:
        if char.isdigit():
            numcheck = True 
    print(numcheck)
    
    for char in s:
        if char.islower():
            lowcheck = True 
    print(lowcheck)
    
    for char in s:
        if char.isupper():
            upcheck = True 
    print(upcheck)

