class Solution(object):
    def searchRange(self, nums, target):
        left=0
        right=len(nums)-1
        mid=0
        flag=-1
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]==target:
                flag=1
                break
            elif target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        if flag==-1:
            return [-1,-1]
        else:
            left=mid
            right=mid
            for i in range(mid-1,-1,-1):
                if nums[i]==target:
                    left=i
            for i in range(mid+1,len(nums),1):
                if nums[i]==target:
                    right=i
            return [left,right]