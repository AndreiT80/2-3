my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = len(my_list)
i = 0
while i < len(my_list):
    if my_list[i] >= 0 and a >= i:
        print(my_list[i])
        i += 1
        continue
    if my_list[i] < 0 and a >= i:
        break
