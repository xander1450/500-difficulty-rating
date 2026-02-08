nums = list(map(int, input().split()))
s=0
i=0
while(i<4):
    if nums[i] >=10:
        s+=1
    i+=1
print(s)
