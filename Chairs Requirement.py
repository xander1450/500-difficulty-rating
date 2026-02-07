for i in range(int(input())):
    s, c = map(int, input().split())
    print(s-c if s-c>=0 else 0)

OR 

for i in range(int(input())):
    s, c = map(int, input().split())
    print(max((x,y),0))
