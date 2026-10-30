class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(0, len(nums)):
        #     init = nums[i]
        #     for j in range(i+1, len(nums)):
        #         if init == nums[j]:
        #             return True
        # return False
        nums = sorted(nums)
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False