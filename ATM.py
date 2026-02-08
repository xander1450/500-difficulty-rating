x, y = map(float, input().split())
if(x%5==0 and x+.50<=y):
    print(f"{y-x-0.50:.2f}")
else:
    print(f"{y:.2f}")
