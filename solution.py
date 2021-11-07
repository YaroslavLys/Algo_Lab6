class Solution:
    answer = 0

    @staticmethod
    def __find_possible_squares(n, x):
        list_of_squares = []
        i = 0
        length = 0
        while len(str(length)) < len(n):
            list_of_squares.append(x ** i)
            length = format(x ** i, "b")
            i += 1
        return list_of_squares

    @staticmethod
    def __find(n, list_of_squares, start):
        bin_square = None
        for j in range(start, len(n) + 1):
            if int(n[(start - 1):j], 2) in list_of_squares:
                bin_square = n[(start - 1):j]
        if bin_square is not None:
            print(bin_square)
            Solution.answer += 1
            start = start + len(bin_square)
            Solution.__find(n, list_of_squares, start)

    @staticmethod
    def solve(n, x):
        list_of_squares = Solution.__find_possible_squares(n, x)
        Solution.__find(n, list_of_squares, 1)
        answer = Solution.answer
        Solution.answer = 0
        return answer
