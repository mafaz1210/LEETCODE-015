class Solution:
    def specialGrid(self, n: int):
        size = 2 ** n
        grid = [[0] * size for _ in range(size)]
        
        def fill(row, col, side, start):
            if side == 1:
                grid[row][col] = start
                return
            
            half = side // 2
            quad_count = half * half
            
            # Order: top-right, bottom-right, bottom-left, top-left
            fill(row, col + half, half, start)                    # top-right
            fill(row + half, col + half, half, start + quad_count)  # bottom-right
            fill(row + half, col, half, start + 2 * quad_count)     # bottom-left
            fill(row, col, half, start + 3 * quad_count)            # top-left
        
        fill(0, 0, size, 0)
        return grid