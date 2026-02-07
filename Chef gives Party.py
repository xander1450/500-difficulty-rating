for i in range(int(input())):
    n,x,k=map(int, input().split())
    print("YES" if n*x<=k else "NO")
