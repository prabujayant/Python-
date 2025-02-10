class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t=m*n

        l=0
        r=t-1

        while l<=r:
            mid = l+(r-l)//2
            if mid==target:
                return True

            elif mid < target:
                l=mid+1

            else:
                r=mid-1

        return False



        
