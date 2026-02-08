for i in range(int(input())):
    num = list(map(int, input().split()))
    s = sorted(num)
    print( "YES" if s[0]+s[1] < s[2] else "NO")
