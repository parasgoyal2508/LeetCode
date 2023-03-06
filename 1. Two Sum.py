class Solution(object):
    def twoSum(self, nums, target):

        seen = {}
        for i in range(len(nums)):
           remaining = target - nums[i]
           if remaining in seen:
               return [i, seen[remaining]]
           seen[nums[i]] = i 