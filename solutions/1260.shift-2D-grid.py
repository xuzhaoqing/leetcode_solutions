class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not grid:
            return []
        grid = [list(x) for x in zip(*grid)]
        
        for _ in range(k):
            last = grid[-1]
            last = [last[-1]] + last[:-1]
            grid = [last] + grid[:-1]
        return [list(x) for x in zip(*grid)]
            