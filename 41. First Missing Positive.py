class Solution(object):
    def firstMissingPositive(self, nums):
        vset=set(nums)
        for i in range(1,len(nums)+1):
            if i not in vset:
                return i
        return len(nums)+1