class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        self.nums = nums
        dict = {}
        for num in self.nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        for x in dict:
            if dict[num] == 1:
                return num
            
sol = Solution()

print(sol.singleNumber({4,1,2,2,1}))