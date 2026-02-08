for i in range(int(input())):
    x,y = map(int, input().split())
    print("YES" if x*1.07>=y else "NO")
