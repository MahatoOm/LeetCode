class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        answer = []
        i=j=0
        m = len(nums1)
        n = len(nums2)
        while i < m and j < n:

        
            if nums1[i][0] == nums2[j][0] :
                answer.append([nums1[i][0], nums1[i][1] + nums2[j][1]  ])
                i+=1
                j+=1
            elif nums1[i][0] < nums2[j][0] :
                answer.append( [nums1[i][0], nums1[i][1]])
                i+=1
            elif nums1[i][0] > nums2[j][0]:
                answer.append( [nums2[j][0], nums2[j][1]])

                j+=1
                
        while  i<m:
            answer.append( [nums1[i][0], nums1[i][1]])
            i+=1
        while j<n:
            answer.append( [nums2[j][0], nums2[j][1]])
            j+=1

        return answer
