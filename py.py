n = int(input("Enter a number: "),)
b = 0
n1=n
while n1 > 0:
   a = n1 % 10
   b= b * 10+a
   n1 //= 10
if n1 == sum:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")