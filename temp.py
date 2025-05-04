def fu(lst):
    lst = [4, 6, 3, 4, 5]
    string = ''
    for i in range(len(lst)):
        value = lst[i]
        is_end = i == len(lst) - 1
        string += str(value)
        if not is_end:
            string += ', '

a = abs(-23)
print(a)
