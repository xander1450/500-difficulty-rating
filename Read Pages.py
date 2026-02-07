for i in range(int(input())):
    n,x,y=map(int,input().split())
    print("YES" if (n/x)<=y else "NO")
