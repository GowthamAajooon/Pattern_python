n = int(input())
m=1
n1=[]
for i in range(1,n+1):
    n2=[]
    for j in range(1,i+1):
        if j==1:
            n2.append(str(m))
            print(m,end="")
        else:
            n2.append("*"+str(m))
            print("*"+str(m),end="")
        m+=1
    n1.append(n2)
    print()
n1=n1[::-1]
for i in n1:
    print("".join(i))

    
    
    
1
2*3
4*5*6
4*5*6
2*3
1
