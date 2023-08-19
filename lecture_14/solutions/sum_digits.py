def sum_digs(val):
    s = 0
    while val > 0:
        if val != 0:
            dig = val % 10
            s += dig
            val = val // 10
    return s


print(sum_digs(10209))