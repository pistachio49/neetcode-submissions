class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        arr = []
        ans = []

        for num in c:
            heapq.heappush(arr, (-c[num], num))

        for _ in range(k):
            ans.append(heapq.heappop(arr)[1])

        return ans