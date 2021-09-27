from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums:
            ex_i = nums[0]
        for i in nums[1:]:
            if ex_i == i:
                nums.remove(i)
            ex_i = i

        return len(nums)



s = Solution()

print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))