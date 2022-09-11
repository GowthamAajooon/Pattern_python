n = int(input())
for i in range(1,n+1):
    for j in range(i,n+1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    for j in range(1,i):
        print("*",end="")
    print()
for i in reversed(range(1,n)):
    for j in reversed(range(i,n+1)):
        print(" ",end="")
    for j in reversed(range(1,i+1)):
        print("*",end="")
    for j in reversed(range(1,i)):
        print("*",end="")
    print()
print()

'''
  *
 ***
*****
 ***
  *
  '''
