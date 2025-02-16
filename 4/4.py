def main(s, p):
    if len(s) > 10**5 and len(p) > 10**4:
        return None
    arr1 = list(s)
    arr2 = list(p)
    if sorted(arr1) == sorted(arr2) :
        return True
    return False
print(main("12", "12"))
print(main("12q", "21"))