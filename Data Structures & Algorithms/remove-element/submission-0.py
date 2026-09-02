class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        found = {}
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
                found[count] = i
        copy = len(nums) - count
        while count != 0:
            nums.append(nums.pop(found[count]))
            count -= 1
        return copy