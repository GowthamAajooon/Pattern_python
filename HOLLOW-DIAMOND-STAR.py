n = int(input())

for i in range(n):
    print("  "*(n-i-1)+"*",end=" ")
    if i >= 1:
        print("  "*(2*i-1)+"*",end=" ")
    print()
for i in reversed(range(n-1)):
    print("  "*(n-i-1)+"*",end=" ")
    if i >= 1:
        print("  "*(2*i-1)+"*",end=" ")
    print()
