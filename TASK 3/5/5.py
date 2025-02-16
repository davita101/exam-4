def main(arr):
    res = []
    for i in range(len(arr)):
        x = 1
        for k in range(len(arr)):
            if arr[i] != arr[k]:
                x *= arr[k]
        res.append(x)
    return res        
                
print(main([1,2,3,4]))