class Solution(object):
    def findMin(self, nums):
        n =len(nums);
        if (n == 1):
            return nums[0];
        if (n == 2):
            if nums[0]>nums[1]:
                return nums[1]
            else:
                return nums[0]
            
        if (nums[0] < nums[n - 1]):
            return nums[0]
        l=0
        r=len(nums)-1
        while(l<=r):
            mid=l+(r-l)//2
            prev=(mid-1+n)%n
            next=(mid+1)%n
            if nums[mid]<=nums[prev] and nums[mid]<=nums[next]:
                return nums[mid]
            else:
                if nums[mid]>=nums[l] and nums[mid]<=nums[r]:
                    return nums[l]
                elif nums[mid]>=nums[l]:
                    l=mid+1
                elif nums[mid]<=nums[r]:
                    r=mid-1