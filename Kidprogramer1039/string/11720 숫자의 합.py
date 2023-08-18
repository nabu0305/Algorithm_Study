import sys
a = int(sys.stdin.readline())
b = sys.stdin.readline().rstrip()
result = 0
for i in b:
    result = result + int(i)
    
print(result)
