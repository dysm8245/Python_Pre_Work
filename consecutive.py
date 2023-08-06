def is_consecutive(a_list):
    if len(a_list) == 0 or a_list == None:
        return False
    for i in range(len(a_list)):
        if i != len(a_list)-1:
            if a_list[i] + 1 != a_list[i+1]:
                return False
    return True
result = is_consecutive([1,2,3,4,5,6])
result2 = is_consecutive([3, 7, 9])
print(result)
print(result2)