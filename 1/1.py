def main(arr):
    x = len(arr) // 2 #! ლუიწი
    
    if len(arr) % 2 == 1:
        x = len(arr) // 2 + 1 #! კენტი
        
    for i in arr:
        if arr.count(i) == x:
            return i
    return None
print(main([1,2,4,5,9,9,9,9,9])) # kenti
print(main([1,2,4,1,8,8,8,8])) # luwi