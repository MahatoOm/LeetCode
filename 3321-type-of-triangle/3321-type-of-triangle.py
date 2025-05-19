class Solution:
    def triangleType(self, num: List[int]) -> str:
        

        if num[0] == num[1] == num[2]:
            return "equilateral"

        elif (num[0] == num[1] and num[0] +  num[1] >  num[2] ) or (num[0] == num[2] and num[0] + num[2] > num[1] )or (num[1] == num[2] and num[1] + num[2] > num[0]):
            return "isosceles"

        elif num[0] +  num[1] >  num[2] and num[1] + num[2] > num[0] and num[0] + num[2] > num[1]:
            return "scalene"

        else:
            return "none"