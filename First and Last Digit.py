for i in range(int(input())):
    n = int(input())
    last = n%10
    x =0
    while(n>0):
        x = n%10
        n=n//10
    first = x
    print(last+first)
