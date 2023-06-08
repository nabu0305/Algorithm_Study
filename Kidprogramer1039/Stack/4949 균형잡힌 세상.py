while True:
    stc = input()
    stk = []
    
    if stc == ".":
        break

    for j in stc:
        if j == '(' or j == '[':
            stk.append(j)
        elif j == ')':
            if len(stk) != 0 and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(')')
                break
        elif j == ']':
            if len(stk) != 0 and stk[-1] == '[':
                stk.pop()
            else:
                stk.append(']')
                break            
    if len(stk) == 0:
        print('yes')
    else:
        print('no')
