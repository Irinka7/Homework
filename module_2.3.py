my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len_list = len(my_list)
a = 0
x = 0
while a >= 0:
    a = my_list[x]
    if a == 0:
        x = x + 1
        continue
    if a > 0:
        print(a)
    x = x + 1
    if x > len_list:
        break





