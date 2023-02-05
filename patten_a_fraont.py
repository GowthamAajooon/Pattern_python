n = int(input())
for i in range(1,n+1):
    m,f=1,[]
    for j in range(n,i-1,-1):
        print(chr(64+m),end="")
        f.append(chr(64+m))
        m+=1
    for j in range(2,i+1):
        print("  ",end="")
    f=f[::-1]
    print("".join(f),end="")
    print()
