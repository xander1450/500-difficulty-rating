for i in range(int(input())):
    n,m,k= map(int, input().split())
    print("YES" if m-k-n>=0 else "NO")
