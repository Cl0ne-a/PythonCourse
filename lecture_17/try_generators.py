def factors(n):
    for val in range(1, n + 1):
        if n % val == 0:
            yield val


factors_of_20 = factors(20)
print(next(factors_of_20))
print(next(factors_of_20))
print(next(factors_of_20))
print(next(factors_of_20))
print(next(factors_of_20))

