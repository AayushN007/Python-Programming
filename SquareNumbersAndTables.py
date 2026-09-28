#1 Sqyare numbers
 
n = (int(input("Enter the value of n: ")))
print("the first ",n," square numbers are:")
for i in range(1, n+1):
    print(i * i, end=" ")
    
#2 tables for particular number

n = (int(input("\nEnter the value of n: ")))
print("the table of ",n," is:")
for i in range(1, 11):
    print(n, "x", i, "=", n*i)