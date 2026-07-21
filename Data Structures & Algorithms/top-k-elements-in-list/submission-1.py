class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for num in nums:
            check = num
            if check not in store:
                store[num] = 1
            else:
                store[num] += 1
        topKeys = sorted(store, key=store.get, reverse=True)[:k]
        return topKeys