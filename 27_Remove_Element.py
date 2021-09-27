from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # for i in nums[:]:
        #     if i == val:
        #         nums.remove(i)

        # return len(nums)

        while val in nums:
            nums.remove(val)
        return len(nums)

s = Solution()

print(s.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))