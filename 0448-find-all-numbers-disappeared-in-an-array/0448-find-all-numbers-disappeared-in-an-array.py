class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing_numbers = []
        set_nums = set(nums)
        for num in range(1,len(nums)+1):
            if  num not in set_nums:
                missing_numbers.append(num)
        return missing_numbers        
            
        
        