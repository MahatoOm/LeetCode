class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = version1.split(".")
        version2 = version2.split(".")
        i , j = 0, 0
        while i < len(version1) and i < len(version2):
           
            
            if int(version1[i]) < int(version2[i]) :
                return -1
            if int(version1[i]) > int(version2[i]):
                return 1
            i += 1
        j = i
        while i < len(version1):
            if int(version1[i]) > 0:
                return 1
            if int(version1[i]) < 0:
                return -1
            i +=1

        while j < len(version2):
            if int(version2[j]) < 0:
                return 1   
            if int(version2[j]) > 0:
                return -1   
            j += 1  
            
        return 0