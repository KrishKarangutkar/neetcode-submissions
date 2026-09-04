class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        appear = {}
        for n in nums[:]:
            if n in appear:
                nums.remove(n)
            else:
                appear[n] = 0
        return len(nums)