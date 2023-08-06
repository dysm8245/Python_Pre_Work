def hello_name(user_name):
    print("hello_" + user_name)
hello_name("Dylan")

def first_odds():
    odds = ""
    for i in range(100):
        if i%2 == 1:
            odds = odds + str(i) + ", "
    print(odds)
first_odds()

def max_num_in_list(a_list):
    max = a_list[0]
    for i in a_list:
        if i >= max:
            max = i
    return max
max = max_num_in_list([1,5,25, 100, 34])
print(max)

def is_leap_year(a_year):
    if a_year%4 == 0 and a_year%100 != 0:
        return True
    if a_year%100 == 0 and a_year%400 == 0:
        return True
    else:
        return False

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

