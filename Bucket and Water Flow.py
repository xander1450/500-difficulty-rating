for i in range(int(input())):
    w,x,y,z = map(int, input().split())
    if(x-(w+(y*z))==0):
        print("filled")
    elif(x-(w+(y*z))>0):
        print("unfilled")
    else:
        print("overflow")
