def count_fact(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


if __name__ == "__main__":
    for k in range(1, 10000 + 1):
        n = k
        res = count_fact(n)
        if res == 2:
            print(n)