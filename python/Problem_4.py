# Find the largest palindrome made from the product of two 3-digit numbers.
# E.g. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.


def create_multipliers(nb_size):
    lst = [int(x) for x in str(9)]
    for i in range(nb_size - 1):
        lst.append(9)

    return "".join(map(str, lst))


def palindrome_product(nb_size):
    a = create_multipliers(nb_size)
    b = create_multipliers(nb_size)
    product_palindrome = [int(x) for x in str(a * b)]
    print('hey')
    # while True:
    # product_palindrome[:len(product_palindrome/2)]
    # if product_palindrome.l


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for row_num in range(numRows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle


if __name__ == '__main__':
    # palindrome_product(3)
    test = Solution()
    print(test.generate(6))
