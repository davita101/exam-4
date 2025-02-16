def main(arr):
    x = []
    for i in range(min(arr), max(arr)+1):
        x.append(i)
    if x == arr:
        return arr
    #! missing number
    for missing in x:
        if missing not in arr:
            return missing
print(main([-2, -1 , 0, 2, 4]))
print(main([-2, -1 , 0, 1, 2, 3, 4]))