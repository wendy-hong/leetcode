class Solution:
    def longestPalindrome_sol1(self, s: str) -> str:
        # Execution time: 5776 ms, defeat 37.25% of all Python users
        # Memory consumption: 23.4 MB, defeat 7.02% of all Python users
        # Test cases passed: 180/180
        # If a substring is palindromic, then it is also palindromic after removing both the first and the last letters.
        # P(i,j) = P(i+1,j-1) ^ (Si==Sj)
        n = len(s)
        if n < 2:
            return s
        ans = s[0]
        table = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            table[i][i] = 1
            if i < (n - 1) and s[i] == s[i + 1]:
                table[i][i + 1] = 1
                ans = s[i:i + 2]
        for i in range(2, n):
            for j in range(n - i):
                if table[j + 1][j + i - 1] and s[j] == s[j + i]:
                    table[j][j + i] = 1
                    if i + 1 > len(ans):
                        ans = s[j:j + i + 1]
        return ans

    def longestPalindrome_sol2(self, s: str) -> str:
        # Execution time: 1164 ms, defeat 58% of all Python users
        # Memory consumption: 15.1 MB, defeat 71% of all Python users
        # Test cases passed: 180/180
        n = len(s)
        ans = []

        def findPalin(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        for i in range(n):
            len1 = len(findPalin(i, i))
            if len1 > len(ans):
                ans = findPalin(i, i)
            len2 = len(findPalin(i, i + 1))
            if len2 > len(ans):
                ans = findPalin(i, i + 1)
        return ans
