for i in range(00, 100):
    if i <= 9:
        i = str(i)
        print("0" + i, end=" ,")
    else:
        print(i, end=" ,")
