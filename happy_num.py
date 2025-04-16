class Solution:
    def isHappy(self, n):
        n = str(n)
        nums_encountered = [n]
        while True:
            num = 0
            for i in range(len(n)):
                num += int(n[i]) * int(n[i])
            if num == 1:
                return True
            else:
                n = str(num)
                if n in nums_encountered:
                    return False
                else:
                    nums_encountered.append(n)

sol = Solution()

print(sol.isHappy(19))