class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t=m*n

        l=0
        r=t-1
        
        while l<=r:
            m = l+(r-l)//2
            i=m//n
            j=m%n
            mid_num=matrix[i][j]
            if mid_num==target:
                return True

            elif mid_num < target:
                l=m+1

            else:
                r=m-1

        return False



        
