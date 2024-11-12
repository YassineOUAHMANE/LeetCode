class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        result = []
        for i,el in enumerate(nums):
            if target - el in hash_map:
                    result.append(hash_map[target-el])
                    result.append(i)   
            else:
                hash_map[el] = i
        return result        
                
                
                