# ****1
# ***23
# **456
# *78910

n = int(input())
a = 1
for i in range(1,n+1):
  for j in range(i,n):
    print("*",end=" ")
  for j in range(1,i+1):
    print(a,end=" ")
    a = a + 1
  print()
