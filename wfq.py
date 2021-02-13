def isValidSudoku(board) -> bool:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        new = ""
        for lists in board:
            new += "".join(lists)
        b = new
        for i in range(0, 73, 9):
            ts = []
            for y in range(9):
                if b[i + y] != ".":
                    ts.append(b[i + y])
            if len(ts) != len(set(ts)):
                return False
        for i in range(9):
            ts = []
            for y in range(0, 73, 9):
                if b[i + y] != ".":
                    ts.append(b[i + y])
            if len(ts) != len(set(ts)):
                return False
        for o in range(0, 56, 27):
            for z in range(0, 7, 3):
                sq = []
                for k in range(3):
                    if b[z + o + k] != ".":
                        sq.append(b[o + z + k])
                    if b[o + z + 9 + k] != ".":
                        sq.append(b[o + 9 + z + k])
                    if b[o + z + 18 + k] != ".":
                        sq.append(b[o + 18 + z + k])
                if len(sq) != len(set(sq)):
                    return False
        return True