class Solution:
    def strStr(self, source, target):
        """
        for each possible search position, we start the search for match. if we find it, return the position. if can not find it after iteration. return -1
        """
        if source is None or target is None  or len(source)<len(target): 
            return -1
        # i is the index of the position to start search
        for i in range(0,len(source) - len(target) + 1):
            
            #j is the idex of character in the target
            j=0
            while j < len(target):
                if target[j] != source[i+j]:
                    break
                j +=1 
            
            if j == len(target):
                return i
        
        return -1