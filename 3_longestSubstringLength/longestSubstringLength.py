class Solution:
    def lengthOfLongestSubstring_sol1(self, s: str) -> int:
        # Execution time: 80 ms, defeat 30.09% of all Python users
        # Memory consumption: 15.1 MB, defeat 21.06% of all Python users
        # Test cases passed: 987/987
        n = len(s)
        if n == 0:
            return 0
        ans = 1
        sub = [s[0]]
        for i in range(1, n):
            if s[i - 1] in sub:
                if s[i] not in sub:
                    sub.append(s[i])
                    if len(sub) > ans:
                        ans = len(sub)
                else:
                    tmp = len(sub)
                    if s[i] == sub[tmp - 1]:
                        sub = [s[i]]
                    else:
                        # for j in range(1, tmp):
                        #     if s[i] == sub[tmp - j - 1]:
                        #         sub = sub[tmp - j:]
                        #         sub.append(s[i])
                        #         break
                        t = sub.index(s[i]) + 1
                        sub = sub[t:]
                        sub.append(s[i])
            else:
                sub = [s[i]]
        return ans

    def lengthOfLongestSubstring_sol2(self, s: str) -> int:
        # Execution time: 68 ms, defeat 48% of all Python users
        # Memory consumption: 15 MB, defeat 69% of all Python users
        # Test cases passed: 987/987
        n = len(s)
        if n == 0:
            return 0
        ans = 1
        tmp = ''
        for i in range(n):
            if s[i] not in tmp:
                tmp = tmp + s[i]
            else:
                m = tmp.index(s[i]) + 1
                tmp = tmp[m:]
                tmp = tmp + s[i]
            ans = max(ans, len(tmp))
        return ans

    def lengthOfLongestSubstring_sol3(self, s: str) -> int:
        occ = set()  # Hash set
        n = len(s)
        rk, ans = -1, 0  # right_pointer_init = -1
        for i in range(n):  # i is the left pointer
            if i != 0:
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                occ.add(s[rk + 1])
                rk += 1
            # from ith to (rk)th, the substring is non-repeated
            ans = max(ans, rk - i + 1)
        return ans
