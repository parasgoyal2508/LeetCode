class Solution(object):
    def missingNumber(self, nums):
        sum=len(nums)
        sumofarray=0
        for i in range(len(nums)):
            sum+=i
            sumofarray+=nums[i]
        return sum-sumofarray