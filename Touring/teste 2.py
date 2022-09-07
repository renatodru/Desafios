def isValid(s: str) ->bool:
    allow = ["{","[","(","}","]",")"]
    test = s
    for caracter in test:
        if caracter not in allow:
            s = s.replace(caracter, "")
               
    allow2 = ["()","[]","{}"]
    change = 1
    while change > 0:
        change = 0
        for k in range(len(s)):            
            if s[k:k+2] in allow2:
                s = s.replace(s[k:k+2], "")
                change += 1
                break

    if len(s) == 0:result = True
    else:result = False
    
    return result

if __name__ == "__main__":
    #line = input()
    
    lines = ["()", "()[]{}", "(]", "([)]", "{[]}{}{{}}({})[]",""]
    
    for line in lines:
        if isValid(line):print("valid")
        else:print("invalid")
        
