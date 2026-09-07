from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            for k, v in Counter(row).items():
                if v > 1 and k != ".":
                    print('1')
                    return False
        
        # Check columns
        for col in range(9):
            c = []
            for r in range(9):
                c.append(board[r][col])
            for k, v in Counter(c).items():
                if v > 1 and k != ".":
                    print(2)
                    return False
        
        # Check squares
        for c in [0,3,6]:
            for r in [0,3,6]:
                print(c,r,board[r][c : c+3] + board[r+1][c:c+3] + board[r+1][c:c+3])
                for k, v in Counter(board[r][c : c+3] + board[r+1][c:c+3] + board[r+2][c:c+3]).items():
                    if v > 1 and k != ".":
                        return False
            
        return True