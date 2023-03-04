class Solution(object):
    def searchInsert(self, nums, target):
        left=0
        right=len(nums)-1
        mid=0
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return left