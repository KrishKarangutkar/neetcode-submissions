class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Map = {}
        for num in nums:
            if num not in Map:
                Map[num] = 1
            else:
                Map[num] += 1
        return max(Map, key=Map.get)