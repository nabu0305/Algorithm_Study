import sys

rep = int(sys.stdin.readline())

for _ in range(rep):
    a = sys.stdin.readline().rstrip()
    print(a[0]+a[len(a)-1])
