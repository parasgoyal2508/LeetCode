class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])
        fi=-1
        l1=0
        r1=m-1
        mid=0
        while(l1<=r1):
            mid=l1+(r1-l1)//2
            if matrix[mid][0]==target:
                return True        
            if matrix[mid][0]<target and mid+1<m and  matrix[mid+1][0]>target:
                fi=mid
                break
            elif matrix[mid][0]>target:
                r1=mid-1
            elif matrix[mid][0]<target:
                l1=mid+1
        l2=0
        r2=n-1
        mid2=0
        while(l2<=r2):
            mid2=l2+(r2-l2)//2
            if matrix[fi][mid2]==target:
                return True
            elif matrix[fi][mid2]>target:
                r2=mid2-1
            elif matrix[fi][mid2]<target:
                l2=mid2+1
        return False