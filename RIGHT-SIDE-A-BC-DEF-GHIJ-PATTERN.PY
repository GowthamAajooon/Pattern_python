# ----A
# ---BC
# --DEF
# -GHIJ
# KLMNO

n = int(input())
a = 65
for i in range(1,n+1):
  for j in range(i,n):
    print("-",end=" ")
  for j in range(1,i+1):
    print(chr(a),end=" ")
    a = a + 1
  print()
