for i in range(int(input())):
    x,y,z = map(int, input().split())
    print((x+y+z)-(max(x,y,z)+min(x,y,z)))

OR 


n = int(input())  
for _ in range(n):
    nums = list(map(int, input().split()))  
    nums.sort()  
    print(nums[1]) 
