n = int(input("Enter the value of n"))
print("the 1st ",n," natural numbers are:")
for i in range(2, 2*n, 2): 
    print(i, end=" ")
print()
print("the first ",n, " odd numbers are:")
for i in range(1, 2*n,2):
    print(i, end=" ")
