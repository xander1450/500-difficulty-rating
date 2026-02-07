for i in range(int(input())):
    w,x,y,z = map(int, input().split())
    print(min((w+x),(y+z)))
