class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visit = set()
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        res = []
        ROWS = len(matrix)
        COLS = len(matrix[0])
        n = ROWS * COLS
        
        idx, i, j = 0, 0, 0
        while len(visit) != n:

            while i >= 0 and i < ROWS and j >= 0 and j < COLS:
                if (i, j) not in visit:
                    res.append(matrix[i][j])
                visit.add((i, j))
                

                dr, dc = direction[idx % 4]
                if (i + dr, j + dc) in visit:
                    break
                
                i += dr
                j += dc
            
            idx += 1
            if i < 0: i = 0
            if i >= ROWS: i = ROWS - 1
            if j < 0: j = 0
            if j >= COLS: j = COLS - 1
        
        return res