class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Row
        for row in range(9):
            rowSet = set()
            for col in range(9):
                if board[row][col] != "." and board[row][col] in rowSet:
                    return False
                if board[row][col] != ".":
                    rowSet.add(board[row][col])
        
        # Col
        for row in range(9):
            colSet = set()
            for col in range(9):
                if board[col][row] != "." and board[col][row] in colSet:
                    return False
                if board[col][row] != ".":
                    colSet.add(board[col][row])
        
        # 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                matrixSet = set()
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        if board[row][col] != "." and board[row][col] in matrixSet:
                            return False
                        if board[row][col] != ".":
                            matrixSet.add(board[row][col])
        
        return True