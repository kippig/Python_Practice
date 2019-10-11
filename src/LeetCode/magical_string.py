class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0

        S = '122'
        p1 = 2
        switch_dict = {'1': '2', '2': '1'}
        counter = 1
        while len(S) < n:
            if switch_dict[S[-1]] == '1':
                counter += int(S[p1])
            S += int(S[p1]) * switch_dict[S[-1]]
            p1 += 1
        if len(S) > n and S[-1] == '1':
            counter -= 1
        return counter, S[: n + 1]


bob = Solution()
print(bob.magicalString(1000))