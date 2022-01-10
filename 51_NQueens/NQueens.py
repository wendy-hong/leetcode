class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Execution time: 96 ms, defeat 24.10% of all Python users
        # Memory consumption: 15.5 MB, defeat 38.31% of all Python users
        # Test cases passed: 9/9
        ans = []
        queens = [0 for _ in range(n)]

        def nqueens(row):
            for column in range(n):
                if check(row, column):
                    queens[row] = column
                    if row == (n - 1):
                        ans.append(num2ans(queens))
                    nqueens(row + 1)
                    queens[row] = 0

        def check(row, column):
            for i in range(row):
                x = queens[i]
                if column == x:
                    return 0
                if (i + x) == (row + column):
                    return 0
                if (i - x) == (row - column):
                    return 0
            return 1

        def num2ans(queens):
            res = []
            for i in range(n):
                tmp = ''
                num = queens[i]
                for j in range(num):
                    tmp += '.'
                tmp += 'Q'
                for j in range(num + 1, n):
                    tmp += '.'
                res.append(tmp)
            return res

        nqueens(0)
        return ans
