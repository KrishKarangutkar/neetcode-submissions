class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for num in nums:
            if num not in store:
                store[num] = 1
            else:
                store[num] += 1
        return sorted(store, key=store.get, reverse=True)[:k]
        