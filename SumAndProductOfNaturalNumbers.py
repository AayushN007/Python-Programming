n = int(input("Enter the value of n :"))
sum = 0
prod = 1
for i in range(1, n+1 ):
    sum = sum + i
    prod = prod * i
print("The sum of first ", n ," nautral numbers is =",sum)
print("The product of first ", n ," nautral numbers is =", prod)