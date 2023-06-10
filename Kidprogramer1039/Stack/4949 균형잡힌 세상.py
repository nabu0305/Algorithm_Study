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
# ---------------------------------------------------------------------------
#4949번 문제
#내가 생각한 풀이코드 수정

import sys

stk = []
res = 0
data = sys.stdin.read().splitlines()
for i in data:
    stc = i
    Sopen = 0 #소괄호 오픈
    Sclose = 0 #소괄호 클로즈
    Bopen = 0 #대괄호 오픈
    Bclose = 0 #대괄호 클로즈
    prev = []
    ep = 0 #마지막 YES 출력 전 미리 출력한 이력이 있는지 확인하기 위한 용도
    if stc[0] == "." and len(stc) == 1:
        break
    else:
        for i in stc:
            if stc[-1] != ".":
                print("no")
                ep += 1
                break
            else:        
                if Sclose > Sopen:
                    print("no")
                    ep += 1
                    break
                elif Bclose > Bopen:
                    print("no")
                    ep += 1
                    break        
                else:
                    if i == "(": #소괄호일 경우, 우선순위 bool 켜주고, 소괄호 개수 추가
                        Sopen += 1
                        prev.append(i)
                    elif i == ")" and not prev:
                        print("no")
                        ep += 1
                        break                    
                    elif i == ")" and prev[-1] == "(":
                        Sclose += 1
                        prev.pop()
                    elif i == ")" and prev[-1] != "(":
                        print("no")
                        ep += 1
                        break               
                    if i == "[":
                        Bopen += 1
                        prev.append(i)
                    elif i == "]" and not prev:
                        print("no")
                        ep += 1
                        break                                 
                    elif i == "]" and prev[-1] == "[":
                        Bclose += 1
                        prev.pop()
                    elif i == "]" and prev[-1] != "[":
                        print("no")
                        ep += 1
                        break
    if ep == 1:
        continue
    else:
        if Sopen == Sclose and Bopen == Bclose:
            print("yes")
        else:
            print("no")
