# append() is a list function 
n = int(input())
c = int(input())
a = []
for i in range(c):
    a.append(n)
    n = n +1
s = 0
for i in range(len(a)):
    s = s + a[i]
print(s)
