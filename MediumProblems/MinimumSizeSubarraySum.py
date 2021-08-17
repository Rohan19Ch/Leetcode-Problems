def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ws = 0
        we = 0
        winSum = 0
        length = len(nums)
        minL = math.inf
        while we < length:
            winSum += nums[we]
            while winSum >= target:
                minL = min(minL, we-ws+1)
                winSum = winSum - nums[ws]
                ws += 1
            we += 1
        if minL == math.inf:
            return 0
        else:
            return minL