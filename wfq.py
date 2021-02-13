def isValidSudoku(board) -> bool:
    # line
    i = 0
    b = board
    new = ""
    for lists in board:
        new.join(lists)
    for i in range(0, 56, 3):
        sq = set(b[i], b[i + 1], b[i + 2], b[i + 9], b[i + 10], b[i + 11],
                 b[i + 18], b[i + 19], b[i + 20])
        sq2 = set(b[i + 1], b[i + 2], b[i + 9], b[i + 10], b[i + 11], b[i + 18],
                  b[i + 19], b[i + 20])
        if len(sq) == len(sq2):
            return False
    while True:
        y = i + 1
        for y in range(9):
            if board[i] == board[y]:
                return False
            if board[i] == board[y * 9]:
                return False

isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])