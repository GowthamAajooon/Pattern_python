n = int(input())+1
for i in range(1,n):
    for i in range(2,i+1):
        print(" ",end="")
    for j in range(n,i,-1):
        print("* ",end="")
    print()
for i in reversed(range(1,n)):
    for i in range(2,i+1):
        print(" ",end="")
    for j in range(n,i,-1):
        print("* ",end="")
    print()
