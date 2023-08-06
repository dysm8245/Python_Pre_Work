def first_odds():
    odds = ""
    for i in range(100):
        if i%2 == 1:
            odds = odds + str(i) + ", "
    print(odds)
first_odds()