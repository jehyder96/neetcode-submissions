class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        result = []

        for idx, value in enumerate(nums):
            complement = target - value

            if complement in seen:
                return [seen[complement], idx]
            else:
                seen[value] = idx