n = int( input())
a = 1
if n < 0:
   print("negative numbers")
elif n == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,n + 1):
       a = a * i #when the index is one can set that
   print(a)
