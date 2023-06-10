import sys

count = 1 #뺀 숫자중에 최상단(어차피 pop을 할 때 이 숫자만 보면 되기 때문)
temp = True #에러 여부
stack = [] #
op = []

input = sys.stdin.readline
N = int(input()) #배열 입력받는 함수

for i in range(N):
    num = int(input()) # 숫자 입력 받기    

    while count <= num: #입력받은 숫자만큼 스택에 넣기
        stack.append(count)
        op.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        temp = False
        break

if temp == False:
    print("NO")
else:
    for i in op:
        print(i)
