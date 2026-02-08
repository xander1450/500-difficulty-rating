for i in range(int(input())):
    x,y=map(int, input().split())
    print(x-y if x>y else y-x)

OR 


t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(abs(x - y))
