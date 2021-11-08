class Solution:
    answer = 0
    no_solution = False

    @staticmethod
    def __find_possible_squares(n, x):
        if x == 1:
            return [1]
        list_of_squares = []
        i = 0
        square = 0
        while square < int(n, 2):
            square = x ** i
            list_of_squares.append(square)
            i += 1
        return list_of_squares

    @staticmethod
    def __find(n, list_of_squares, start):
        bin_square = 0
        for j in range(start, len(n) + 1):
            if int(n[(start - 1):j], 2) in list_of_squares:
                bin_square = n[(start - 1):j]
            if int(str(bin_square), 2) == 0 and j == len(n):
                Solution.no_solution = True
        if int(str(bin_square), 2) != 0:
            print(bin_square)
            Solution.answer += 1
            start = start + len(bin_square)
            Solution.__find(n, list_of_squares, start)

    @staticmethod
    def solve(n, x):
        list_of_squares = Solution.__find_possible_squares(n, x)
        Solution.__find(n, list_of_squares, 1)
        if not Solution.no_solution:
            answer = Solution.answer
            Solution.answer = 0
            return answer
        else:
            Solution.answer = 0
            return -1
