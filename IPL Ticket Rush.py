t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    if(n>m):
        print(n-m)
    else:
        print(0)

  OR


for i in range(int(input())):
    print(max(0, n-m))
