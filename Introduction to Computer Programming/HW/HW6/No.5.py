def reverse_num(num):
    str_num = str(num)
    reverse_str_num = str_num[::-1]
    reverse_num = int(reverse_str_num)
    return reverse_num

print(reverse_num(8375))
