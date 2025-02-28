def odd_num(int_in):
    for i in range(int_in + 1):
        if i % 2 != 0:
            print(i)

limit = int(input("Input the limit: "))

odd_num(limit)
