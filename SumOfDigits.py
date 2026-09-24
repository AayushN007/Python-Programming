n = int(input("Enter the number:"))
m = n
sum = 0
while( n!= 0):
    r = n%10
    sum = sum + r
    n = n // 10
print("the sum of digits of ", m, " =", sum)