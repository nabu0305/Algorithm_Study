import sys
import itertools
from itertools import permutations

lis = []
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

for string in range(n):
    lis.append(sys.stdin.readline().rstrip())


x = lis
a = [int(''.join(l)) for l in permutations(x, k)]
b = list(dict.fromkeys(a))

print(len(b))
