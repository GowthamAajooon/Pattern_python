n = int(input())
n1,m=[],1
for i in range(1,n+1):
    n2=[]
    for j in range(1,i+1):
        print(m,end=" ")
        n2.append(str(m))
        m+=1
    n1.append(n2)
    print()
n1 = n1[::-1]
for i in range(len(n1)):
    print(" ".join(n1[i]))
