n = int(input())
if n>1:
    for i in range(1,n+1):
        for j in range(n,i-1,-1):
            print("*",end=" ")
        for j in range(1,i+1):
            print("",end=" ")
        for j in range(1,i):
            print(" ",end="  ")
        for j in range(i,n+1):
            print("*",end=" ")
        print()
    for i in reversed(range(1,n+1)):
        for j in range(n,i-1,-1):
            print("*",end=" ")
        for j in range(1,i+1):
            print("",end=" ")
        for j in range(1,i):
            print(" ",end="  ")
        for j in range(i,n+1):
            print("*",end=" ")
        print()
        
else:
    print("Invalid input")
