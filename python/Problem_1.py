import timeit


def addition(max):
    sum_of_divider = 0
    for i in range(max):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_divider += i
    return sum_of_divider


if __name__ == '__main__':
    print(addition(1000))
    print(sum([i for i in range(1000) if (i % 3 == 0 or i % 5 == 0)]))

    setup = "from __main__ import addition"
    print(timeit.timeit("addition(1000)", setup=setup))
    print(timeit.timeit(stmt="sum([i for i in range(1000) if (i % 3 == 0 or i % 5 == 0)])", setup=""))