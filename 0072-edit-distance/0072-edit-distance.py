import numpy as np
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        ed = np.zeros((m+1,n+1))
        
        for i in range(m-1,-1,-1):
            ed[i,n] = m-i
        for j in range(n-1,-1,-1):
            ed[m,j] = n-j
        
        for j in range(n-1,-1,-1):
            for i in range(m-1,-1,-1):
                if word1[i] == word2[j]:
                    ed[i,j] = ed[i+1,j+1]
                else:
                    ed[i,j] = 1 + min(ed[i+1,j+1],ed[i,j+1], ed[i+1,j])
        return int(ed[0,0])