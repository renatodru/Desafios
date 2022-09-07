def callPoints(ops) -> int:
    while "C" in ops:
        for enum,op in enumerate(ops):
            if op == "C":
                del(ops[enum-1:enum+1])
                break
    
    for enum,op in enumerate(ops):
        if op == "D":ops[enum] = int(ops[enum-1])*2
        elif op == "+":ops[enum] = int(ops[enum-2])+int(ops[enum-1])
        else: ops[enum] = int(op)
    print(ops)
    result = sum(ops)
    if len(ops) == 0:
        result = None
    
    return result


if __name__ == '__main__':
    #line = input()
    #ops = line.strip().split()
    #print(callPoints(["5","2","C","D","+"]))
    print(callPoints(["5","5","C","3","+"]))
    print(callPoints(["5","5","C","3","+","+"]))
    print(callPoints(["5","5","C","3","+","+","6"]))