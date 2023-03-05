class Solution(object):
    def findPeakElement(self, nums):
        if len(nums)==1:return 0
        if len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        left=0
        right=len(nums)-1
        mid=0
        while(left<=right):
            mid=(left+(right-left)//2)
            if mid>0 and mid<len(nums)-1:
                if nums[mid]>=nums[mid-1] and nums[mid]>=nums[mid+1]:
                    return mid
                elif nums[mid]<nums[mid-1]:
                    right=mid-1
                elif nums[mid]<nums[mid+1]:
                    left=mid+1
            if mid==0:
                if nums[mid]>nums[mid+1]:
                    return mid
                else:
                    left=mid+1
            if mid==len(nums)-1:
                if nums[mid]>nums[mid-1]:
                    return mid
                else:
                    right=mid-1 