class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [0] * size * 2
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + size] = nums[i]
        return ans