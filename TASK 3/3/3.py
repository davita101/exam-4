def main(arr, k):
    if len(arr) == 0:
        return []
    
    k = k % len(arr)
    if k == 0:
        return arr[:]
   
    return  arr[-k:] + arr[:-k]
print(main( [1, 2, 3], 2))
print(main( [1, 2, 3], 2))
    