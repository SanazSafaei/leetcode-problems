from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # ---------------------------------------------------------------------
        # hash = {}
        # for idx, val in enumerate(nums):
        #     test = target - val
        #     x = hash.get(test)
        #     if x is None:
        #         hash[val] = idx
        #         continue
        #     return [hash[test], idx]
        # ----------------------------------------------------------------------
        # hash = {}
        # for idx in range(0,len(nums)):
        #     test = target - nums[idx]
        #     x = hash.get(test)
        #     if x is None:
        #         hash[nums[idx]] = idx
        #         continue
        #     return [hash[test], idx]


nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum(nums, target))
