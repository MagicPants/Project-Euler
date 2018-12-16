# What is the largest prime factor of the number 600851475143 ?


def prime_factor(number):
    prime_number = []
    i, multiplication = 1, 1
    while multiplication != number:
        if number % i == 0:
            prime_number.append(i)
            multiplication *= i
            print(i)
        i += 1

    return prime_number


if __name__ == '__main__':
    print(prime_factor(600851475143))
