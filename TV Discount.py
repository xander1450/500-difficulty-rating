for i in range(int(input())):
    a,b,c,d = map(int, input().split())
    if a-c < b-d:
        print("FIRST")
    elif a-c > b-d:
        print("SECOND")
    else:
        print("ANY")
