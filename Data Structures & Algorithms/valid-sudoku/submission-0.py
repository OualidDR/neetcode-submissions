class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # 1. Check each row
        for row in board:
            count = Counter(row)
            for key, value in count.items():
                if key != '.' and value > 1:
                    return False

        # 2. Check each column (transpose trick)
        transposed = [list(col) for col in zip(*board)]
        for col in transposed:
            count = Counter(col)
            for key, value in count.items():
                if key != '.' and value > 1:
                    return False

        # 3. Check each 3x3 block
        for i in range(0, 9, 3):          # block row start (0,3,6)
            for j in range(0, 9, 3):      # block col start (0,3,6)
                block = []
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        block.append(board[x][y])

                count = Counter(block)
                for key, value in count.items():
                    if key != '.' and value > 1:
                        return False

        return True