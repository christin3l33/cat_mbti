def my_max(lst):
    num = lst[0]

    for i in lst:
        if i > num:
            num = i
    return num