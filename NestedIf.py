a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
c = int(input("Enter the value of c :"))
(print(a) if a > c else print(c)) if a>b else print(b) if b > a and b > c else print(c)