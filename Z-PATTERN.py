size = int(input())
for i in range(0,size):
    for j in range(0,size):
        if(i==0 or i==size-1 or i+j == size-1 ):
            print('*',end=' ')
        else:
            print(" ",end=" ")
    print()
    
