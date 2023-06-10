#9012번 문제
#풀이 시간 : 14:21 ~ 14:44

"""
생각한 풀이방식
1. 괄호의 시작이 ')'이거나, '('인 경우는 No 출력
2. 문자열의 크기가 홀수면 No 출력
3. 그리고 오픈 변수를 지정하고, 클로즈 변수를 지정
고려해야 할 조건
* 오픈 변수와 클로즈 변수는 개수가 같아야 함.
(()()
* 실셈 도중 클로즈 변수가 오픈 변수보다 많아지면 무조건 NO 출력
"""

import sys

input = sys.stdin.readline
rep = int(input())
stk = []
res = 0
for _ in range(rep):
    num = list(input().rstrip())
    open = 0
    close = 0
    ep = 0 #마지막 YES 출력 전 미리 출력한 이력이 있는지 확인하기 위한 용도
    if len(num)%2 == 1: #길이가 홀수일 경우 NO 출력
        print("NO")
        ep += 1
        #print(f"case 1, open = {open}, close = {close}, len = {len(num)}, num = {num}") 
    elif num[0] == ")" or num[-1] == "(": #여는 문자, 혹은 닫는 문자가 반대로일 경우 NO 출력
        print("NO")
        ep += 1
        #print(f"case 2, open = {open}, close = {close}, len = {len(num)}")  
    else:
        for i in num:
            if close > open:
                print("NO")
                ep += 1
                break
            else:
                if i == "(":
                    open += 1
                elif i == ")":
                    close += 1
        if ep == 1:
            continue
        else:
            if open == close:
                print("YES")
            elif open != close:
                print("NO")
        
