from heapq import heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We can use heap data structure
        for i in range(len(nums)):
            nums[i] = -nums[i] # O(1) n times so O(n)
        heapq.heapify(nums)
        for i in range(k):  # O(k)
            largest = heapq.heappop(nums)  # log(n)
        return -largest    
            
            
            
        