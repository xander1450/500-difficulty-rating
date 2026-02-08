for i in range(int(input())):
    a,b,c,x = map(int, input().split())
    print("YES" if a+b>=x or a+c>=x or c+b>=x else "NO")
