


if __name__ == "__main__":
    arr=[90,30,20,10,50]
    for i in range(0,len(arr)):
        for k in range(0,len(arr)-1):
            if arr[k] > arr[k + 1]:
                arr[k],arr[k+1]=arr[k+1],arr[k]
    print(arr)

