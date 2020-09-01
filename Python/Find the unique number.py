def find_uniq(arr):
    s = set(arr)
    for element in s:
        if arr.count(element) == 1:
            return element