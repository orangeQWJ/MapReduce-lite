for x in range(90):
    print(x)


def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n - 1)

func(3)
