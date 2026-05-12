class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = []
        for i in range(len(nums)):
            if nums[i] in nums2:
                return True
            else:
                nums2.append(nums[i])
        return False