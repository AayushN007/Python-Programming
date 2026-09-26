n = int(input("Enter the range of numbers : "))

l1 = []
l2 = []
l3 = []

print("The numbers are : ")
for i in range(n):
    l1.append(int(input()))5
    
l2 = list(map(lambda a: a*a ,l1))
l3 = list(filter(lambda a: a%2==0 ,l1))

print(l1)
print(l2)
print(l3)
