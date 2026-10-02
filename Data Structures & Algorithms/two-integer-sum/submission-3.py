class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenVals = {}

        for i, j in enumerate(nums):
            k = target - j
            if k in seenVals:
                return [seenVals[k], i]
            seenVals[j] = i