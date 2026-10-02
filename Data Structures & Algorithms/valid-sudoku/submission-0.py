class Solution(object):
    def isValidSudoku(self, board):
        for r in range(9):
            rowSet = set()
            for c in range(9):
                if board[r][c] != '.' and board[r][c] in rowSet:
                    return False
                if board[r][c] != '.':
                    rowSet.add(board[r][c])
        
        for c in range(9):
            colSet = set()
            for r in range(9):
                if board[r][c] != '.' and board[r][c] in colSet:
                    return False
                if board[r][c] != '.':
                    colSet.add(board[r][c])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                squareSet = set()
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        if board[r][c] != '.' and board[r][c] in squareSet:
                            return False
                        if board[r][c] != '.':
                            squareSet.add(board[r][c])
        
        return True