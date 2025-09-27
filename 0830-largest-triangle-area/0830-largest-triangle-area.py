class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        def calculatearea( x1, y1, x2, y2, x3, y3):

            return 0.5* abs( (x1 * (y2 - y3)) + (x2 *( y3 - y1)) + (x3 *(y1- y2) ))
        
        n = len(points)
        res =0 
        for i in range(n-2) :

            for j in range( i + 1 ,n-1):

                for k in range( j + 1 , n):
                    res = max(res , calculatearea( points[i][0] , points[i][1] ,points[j][0] ,points[j][1] ,points[k][0] ,points[k][1]  ))



        return res