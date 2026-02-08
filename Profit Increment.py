for i in range(int(input())):
    x,y=map(int, input().split())
    if(x%100==0):
        print(x//10+y)
