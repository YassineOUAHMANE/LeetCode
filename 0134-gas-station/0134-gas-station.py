class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        candidate = 0
        remaining = 0
        prev_remaining = 0
        for i in range(len(gas)):
            remaining += gas[i] - cost[i]
            if remaining < 0:
                candidate = i+1
                prev_remaining += remaining
                remaining = 0
        if candidate == len(gas) or remaining + prev_remaining < 0:
            return -1
        else:
            return candidate
        