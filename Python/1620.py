import sys

n, m = map(int, sys.stdin.readline().split())
key_name = {}
key_num = {}
for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    key_name[name] = i
    key_num[i] = name
for _ in range(m):
    inp = sys.stdin.readline().strip()
    if(inp.isdigit()):
        print(key_num[int(inp)])
    else:
        print(key_name[inp])
