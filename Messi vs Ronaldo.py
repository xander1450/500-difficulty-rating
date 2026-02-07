n = list(map(int, input().split()))
if (n[0]*2 + n[1]) > (n[2]*2 + n[3]):
    print("MESSI")
elif (n[0]*2 + n[1]) < (n[2]*2 + n[3]): 
    print("RONALDO")
else:
    print("Equal")
