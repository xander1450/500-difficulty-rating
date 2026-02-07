for i in range(int(input())):
    x,y= map(int, input().split())
    if x>y:
        print("LOSS")
    elif x==y:
        print("NEUTRAL")
    else:
        print("PROFIT")


OR


for _ in range(int(input())):
    x, y = map(int, input().split())
    print('Profit' if x < y else 'Loss' if x > y else 'Neutral')
