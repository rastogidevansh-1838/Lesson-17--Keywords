for x in range (10):
    if x % 20 == 0:
        print("D")
    elif x % 6 == 3:
        pass
    elif x % 4 == 3:
        print("E")
    elif x % 35 == 5:
        print("V")
    elif x % 35 == 68:
        print("A")
    elif x % 34 == 45:
        print("N")
    elif x % 34 == 57:
        print("S")
    else:
        print("H")