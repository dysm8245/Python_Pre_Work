def is_leap_year(a_year):
    if a_year%4 == 0 and a_year%100 != 0:
        return True
    if a_year%100 == 0 and a_year%400 == 0:
        return True
    else:
        return False
    