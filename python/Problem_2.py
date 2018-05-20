# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


def fibonacci_sequence_calculator(max):
    seq = [0, 1]
    ans = 0
    i = 1
    while ans <= max:
        seq.append(seq[i] + seq[i - 1])

        if seq[i] % 2 == 0:
            ans += seq[i]

        i += 1
    return ans


if __name__ == '__main__':
    print(fibonacci_sequence_calculator(4000000))
