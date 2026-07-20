from copy import deepcopy
class Solution:
    def recur(self,mat,m):
        duplicate = deepcopy(mat)
        ret, popped = [], []
        for i in range(m):
            popped.append(duplicate[i].pop())
            if i>0:
                ret += [[popped[i-1]]+duplicate[i]]
            else:
                ret += [duplicate[i]]
        ret[0].insert(0,popped[-1])
        return ret

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= m*n

        for i in range(k):
            grid = self.recur(grid,m)
        return grid
            

        