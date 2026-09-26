rows = 5

k = 1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if k % 2 == 0:
            print(chr(k + 96),end = " ")
        else:
            print(chr(k + 64), end = " ")
        k += 1
    print()




    
rows = 5

for i in range(1, rows + 1):
    k = (i *(i + 1))//2
    for j in range(1, i + 1):
        print(k, end = " ")
        k -= 1
    print()


# or

rows = 5

sum = 0
for i in range(1, rows + 1):
    sum += i
    temp = sum
    for j in range(1, i + 1):
        print(temp, end = " ")
        temp -= 1
    print()