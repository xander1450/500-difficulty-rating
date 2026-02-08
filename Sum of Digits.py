for i in range(int(input())):
    n = int(input())
    sum = 0
    while n>0:
        sum = n%10+sum
        n=n//10
    print(sum)
