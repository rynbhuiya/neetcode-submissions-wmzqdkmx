class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(row, col, i):
            if i == len(word) - 1 and board[row][col] == word[i]:
                return True
            
            # updated visited db
            visited[(row, col)] = True
            if board[row][col] == word[i]:
                # explore left option
                leftOption = False
                if col - 1 >= 0 and not visited[(row, col - 1)]:
                    leftOption = dfs(row, col - 1, i + 1)
                    visited[(row, col - 1)] = False
                # explore right option
                rightOption = False
                if col + 1 < len(board[row]) and not visited[(row, col + 1)]:
                    rightOption = dfs(row, col + 1, i + 1)
                    visited[(row, col + 1)] = False

                # explore bottom option
                bottomOption = False
                if row + 1 < len(board) and not visited[(row + 1, col)]:
                    bottomOption = dfs(row + 1, col, i + 1)
                    visited[(row + 1, col)] = False
                
                # explore top option
                topOption = False
                if row - 1 >= 0 and not visited[(row - 1, col)]:
                    topOption = dfs(row - 1, col, i + 1)
                    visited[(row - 1, col)] = False
                
                return leftOption or rightOption or bottomOption or topOption
        
            return False
        
        res = False
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    visited = defaultdict(bool)
                    ret = dfs(row, col, 0)
                    res = res or ret
        
        return res