class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for i in row:
                if i in s:
                    return False
                elif i !='.':
                    s.add(i)

        for column in range(len(board)):
            s = set()
            for row in range(len(board[column])):
                i = board[row][column]
                if i in s:
                    return False
                elif i !='.':
                    s.add(i)
        for current in range(len(board)):
            rowindex = 3 * (current % 3)
            colindex = 3 * (current // 3)
            s = set()
            for row in range(rowindex, rowindex+3):
                for col in range(colindex, colindex+3):
                    i = board[row][col]
                    if i in s:
                        return False
                    elif i !='.':
                        s.add(i)
        return True

        