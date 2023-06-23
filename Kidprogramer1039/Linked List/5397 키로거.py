import sys

rep = int(sys.stdin.readline())

for _ in range(rep):
    str1 = []
    str2 = []
    klg = map(str, sys.stdin.readline().rstrip())
    for i in klg:
        if i == "<":
            if str1:
                str2.append(str1.pop())
            else:
                continue
        elif i == ">":
            if str2:
                str1.append(str2.pop())
            else:
                continue
        elif i == "-":
            if str1:
                str1.pop()
        else:
            str1.append(i)
    print(''.join(str1 + list(reversed(str2))))
