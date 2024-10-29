class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        n = len(nums)
        for el in nums:
            if el not in hash_map:
                hash_map[el] = 1
            else:
                hash_map[el] += 1
        for el,count in hash_map.items():
            if count > n//2:
                return el

                  

        