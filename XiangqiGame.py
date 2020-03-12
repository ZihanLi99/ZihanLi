# Author: Zihan Li
# Date: 2020/3/10
# Description: a class named XiangqiGame for playing an abstract board game called xiangqi

from typing import Tuple, List


class PieceType:
    BING = 1
    SHUAI = 2
    MA = 3
    PAO = 4
    XIANG = 5
    SHI = 6
    CHE = 7


class Piece:

    def __init__(self, type, role) -> None:
        super().__init__()
        self.pieceType = type
        self.role = role


class XiangqiGame:
    board: List[List[Piece]]

    def __init__(self) -> None:
        super().__init__()
        self.state = 'UNFINISHED'
        self.board = []
        for r in range(10):
            row = []
            for c in range(9):
                row.append(None)
            self.board.append(row)

        self.board[0][0] = Piece(PieceType.CHE, 'red')
        self.board[0][1] = Piece(PieceType.MA, 'red')
        self.board[0][2] = Piece(PieceType.XIANG, 'red')
        self.board[0][3] = Piece(PieceType.SHI, 'red')
        self.board[0][4] = Piece(PieceType.SHUAI, 'red')
        self.board[0][5] = Piece(PieceType.SHI, 'red')
        self.board[0][6] = Piece(PieceType.XIANG, 'red')
        self.board[0][7] = Piece(PieceType.MA, 'red')
        self.board[0][8] = Piece(PieceType.CHE, 'red')

        self.board[2][1] = Piece(PieceType.PAO, 'red')
        self.board[2][7] = Piece(PieceType.PAO, 'red')

        self.board[3][0] = Piece(PieceType.BING, 'red')
        self.board[3][2] = Piece(PieceType.BING, 'red')
        self.board[3][4] = Piece(PieceType.BING, 'red')
        self.board[3][6] = Piece(PieceType.BING, 'red')
        self.board[3][8] = Piece(PieceType.BING, 'red')

        self.board[6][0] = Piece(PieceType.BING, 'black')
        self.board[6][2] = Piece(PieceType.BING, 'black')
        self.board[6][4] = Piece(PieceType.BING, 'black')
        self.board[6][6] = Piece(PieceType.BING, 'black')
        self.board[6][8] = Piece(PieceType.BING, 'black')

        self.board[7][1] = Piece(PieceType.PAO, 'black')
        self.board[7][7] = Piece(PieceType.PAO, 'black')

        self.board[9][0] = Piece(PieceType.CHE, 'black')
        self.board[9][1] = Piece(PieceType.MA, 'black')
        self.board[9][2] = Piece(PieceType.XIANG, 'black')
        self.board[9][3] = Piece(PieceType.SHI, 'black')
        self.board[9][4] = Piece(PieceType.SHUAI, 'black')
        self.board[9][5] = Piece(PieceType.SHI, 'black')
        self.board[9][6] = Piece(PieceType.XIANG, 'black')
        self.board[9][7] = Piece(PieceType.MA, 'black')
        self.board[9][8] = Piece(PieceType.CHE, 'black')

    def get_game_state(self) -> str:
        return self.state

    def is_in_check(self, role) -> bool:
        if self.state == 'BLACK_WON' and role == 'black':
            return True
        if self.state == 'RED_WON' and role == 'red':
            return True
        return False

    def make_move(self, start, end):
        if self.is_valid_pos(start) and self.is_valid_pos(end):
            row_s, col_s = self.pos_to_rc(start)
            row_e, col_e = self.pos_to_rc(end)

            # do move
            if self.board[row_e][col_e] is not None:
                if self.board[row_e][col_e].role == 'red':
                    self.state = 'BLACK_WON'
                elif self.board[row_e][col_e].role == 'black':
                    self.state = 'RED_WON'
            self.board[row_e][col_e] = self.board[row_s][col_s]
            self.board[row_s][col_s] = None
            return True
        else:
            return False

    def range_horizon_count(self, row, col1, col2):
        start = min(col1, col2)
        end = max(col1, col2)
        count = 0
        for c in range(start + 1, end):
            if self.board[row][c] is not None:
                count += 1
        return count

    def range_vertical_count(self, col, row1, row2):
        start = min(row1, row2)
        end = max(row1, row2)
        count = 0
        for r in range(start + 1, end):
            if self.board[r][col] is not None:
                count += 1
        return count

    def is_valid_move(self, start, end):
        if self.is_valid_pos(start) and self.is_valid_pos(end):
            row_s, col_s = self.pos_to_rc(start)
            row_e, col_e = self.pos_to_rc(end)
            startpiece: Piece = self.board[row_s][col_s]
            if startpiece:
                if startpiece.pieceType == PieceType.XIANG:
                    return abs(row_s - row_e) == 2 and abs(col_s - col_e)
                elif startpiece.pieceType == PieceType.BING:
                    if row_s < 5 and startpiece.role == 'red':
                        return row_e == row_s + 1 and col_s == col_e
                    elif row_s >= 5 and startpiece.role == 'red':
                        return row_e > row_s or col_s != col_e
                    elif row_s < 5 and startpiece.role == 'black':
                        return row_e < row_s or col_s != col_e
                    elif row_s >= 5 and startpiece.role == 'black':
                        return row_e == row_s - 1 and col_s == col_e
                    return False
                elif startpiece.pieceType == PieceType.CHE:
                    if row_s != row_e and col_s == col_e:
                        if self.range_vertical_count(col_s, row_s, row_e) == 0:
                            return True
                    if row_s == row_e and col_s != col_e:
                        if self.range_horizon_count(row_s, col_s, col_e) == 0:
                            return True
                    return False
                elif startpiece.pieceType == PieceType.PAO:
                    if self.board[row_e][col_e] is not None:
                        if row_s != row_e and col_s == col_e:
                            if self.range_vertical_count(col_s, row_s, row_e) == 1:
                                return True
                        if row_s == row_e and col_s != col_e:
                            if self.range_horizon_count(row_s, col_s, col_e) == 1:
                                return True
                        return False
                    else:
                        if row_s != row_e and col_s == col_e:
                            if self.range_vertical_count(col_s, row_s, row_e) == 0:
                                return True
                            if row_s == row_e and col_s != col_e:
                                if self.range_horizon_count(row_s, col_s, col_e) == 0:
                                    return True
                        return False
                elif startpiece.pieceType == PieceType.SHI:
                    if abs(row_s - row_e) == 1 and abs(col_s - col_e) == 1:
                        if startpiece.role == 'black' and (row_e, col_e) in [(7, 3), (7, 5), (8, 4), (9, 3), (9, 5)]:
                            return True
                        elif startpiece.role == 'red' and (row_e, col_e) in [(0, 3), (0, 5), (1, 4), (2, 3), (2, 5)]:
                            return True
                    return False
                elif startpiece.pieceType == PieceType.MA:
                    if abs(row_s - row_e) == 1 and abs(col_s - col_e) == 2:
                        if self.board[row_s][(col_e + col_s) // 2] is None:
                            return True
                    if abs(row_s - row_e) == 2 and abs(col_s - col_e) == 1:
                        if self.board[(row_e + row_s) // 2][col_s] is None:
                            return True
                    return False
                elif startpiece.pieceType == PieceType.XIANG:
                    if abs(row_s - row_e) == 2 and abs(col_s - col_e) == 2:
                        if startpiece.role == 'black' and row_e >= 5:
                            return True
                    if abs(row_s - row_e) == 2 and abs(col_s - col_e) == 1:
                        if startpiece.role == 'red' and row_e < 5:
                            return True
                    return False
                elif startpiece.pieceType == PieceType.SHUAI:
                    if abs(row_s - row_e) == 1 and abs(col_s - col_e) == 0:
                        return True
                    if abs(row_s - row_e) == 0 and abs(col_s - col_e) == 1:
                        return True
                    return False

        return False

    def is_valid_pos(self, pos) -> bool:
        if len(pos) == 2 or len(pos) == 3:
            col = ord(pos[0]) - ord('a')
            row = int(pos[1:])
            return 1 <= col <= 9 and 1 <= row <= 10
        return False

    def pos_to_rc(self, pos) -> Tuple[int, int]:
        col = ord(pos[0]) - ord('a')
        row = int(pos[1:])
        return int(row) - 1, int(col) - 1
