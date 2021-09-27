from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            i = nums.index(target)
            return i
        except:
            for i in range(len(nums)):
                if nums[i]>=target:
                    return i
                elif i == len(nums)-1:
                    return i+1


s = Solution()
print(s.searchInsert(nums = [1,3,5,6], target = 5))