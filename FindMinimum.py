def find_min(arr):
    min = 100
    for ele in arr:
        if ele < min:
            min = ele
    return min



if __name__ == "__main__":
    arr = [10,20,30]
    res = find_min(arr)
    print(res)    
