import itertools

class Solution:
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in itertools.combinations(nums, 2):
            if self.comb_test(i) == target:
                return self.index(nums, i)

    def comb_test(self, comb):
        return sum(comb)

    def index(self, nums, comb):
        index = nums.index(comb[0])
        nums[index] = None
        index2 = nums.index(comb[1])
        return [index, index2]

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
