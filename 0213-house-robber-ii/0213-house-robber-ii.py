class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
                return nums[0]
        if n==0:
                return 0
        skip_last_house = [0]*(n-1)
        skip_first_house = [0]*(n-1)
        for i in range(len(nums)-1):
            skip_last_house.append(nums[i])
            skip_first_house.append(nums[i+1])
        def house_robber(array):
            n = len(array)
            dp = [0]*n
            dp[0] = array[0]
            dp[1] = max(array[0],array[1])
            for i in range(2,n):
                dp[i] = max(array[i] + dp[i-2],dp[i-1])
            return dp[n-1]
        return max(house_robber(skip_last_house),house_robber(skip_first_house))
                
                
        