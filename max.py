def max_num_in_list(a_list):
    max = a_list[0]
    for i in a_list:
        if i >= max:
            max = i
    return max
max = max_num_in_list([1,5,25, 100, 34])
print(max)