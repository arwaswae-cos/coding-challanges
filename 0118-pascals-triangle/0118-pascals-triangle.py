class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            L = [[1], [1,1]]
            for i in range(numRows-2):
                s = [1]+[L[-1][j]+L[-1][j+1] for j in range(len(L[-1])-1)]+[1]
                L.append(s)
        return L