class Solution(object):
    def singleNonDuplicate(self, nums):

        if len(nums)==1:
            return nums[0]
        left=0
        right=len(nums)-1
        mid=0
        while(left<right):
            mid=left+(right-left)//2
            if nums[mid]==nums[mid+1]:
                mid=mid-1
            if ((mid-left+1)%2)==0:
                left=mid+1
            else:
                right=mid
        return nums[left]