def rev(arr):
    res = []
    for i in range(len(arr)-1,-1,-1):
        res.append(arr[i])
    return res

    
if __name__ == "__main__":
    arr = [-10,20,-30]
    res=rev(arr)
    print(res)
    
    
    
    