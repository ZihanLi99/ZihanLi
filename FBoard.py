# Author: Zihan Li
# Date: 2019/12/4
# Description:  a class named FBoard for playing a game, where player x is trying to get her piece to 
#               row 7 and player o is trying to make it so player x doesn't have any legal moves. 

class FBoard:
    def __init__(self):
        self.data = []
        self.game_state = 'UNFINISHED'
        self.xpos = (0, 3)
        for i in range(8):
            self.data.append([' '] * 8)
        self.data[0][3] = 'x'
        self.data[7][0] = 'o'
        self.data[7][2] = 'o'
        self.data[7][4] = 'o'
        self.data[7][6] = 'o'

    def get_game_state(self):
        return self.game_state

    def can_move_x(self, row, col):
        if abs(row - self.xpos[0]) == 1 and \
                abs(col - self.xpos[1]) == 1:
            if 0 <= row < 8 and 0 <= col < 8:
                if self.data[row][col] == ' ':
                    return True
        return False

    def move_x(self, row, col):
        if self.game_state == 'UNFINISHED':
            if self.can_move_x(row, col):
                self.data[self.xpos[0]][self.xpos[1]] = ' '
                self.data[row][col] = 'x'
                self.xpos = (row, col)
                if row == 7:
                    self.game_state = 'X_WON'
                return True
        return False

    def move_o(self, row1, col1, row2, col2):
        if self.game_state == 'UNFINISHED':
            if 0 <= row1 < 8 and 0 <= col1 < 8 and 0 <= row2 < 8 and 0 <= col2 < 8:
                if self.data[row1][col1] == 'o' and self.data[row2][col2] == ' ':
                    if abs(row1 - row2) == 1 and abs(col1 - col2) == 1:
                        if row2 < row1:
                            self.data[row1][col1] = ' '
                            self.data[row2][col2] = 'o'
                            if self.is_o_won():
                                self.game_state = 'O_WON'
                            return True
        return False

    def is_o_won(self):
        row = self.xpos[0]
        col = self.xpos[1]
        if self.can_move_x(row - 1, col - 1) or \
                self.can_move_x(row - 1, col + 1) or \
                self.can_move_x(row + 1, col - 1) or \
                self.can_move_x(row + 1, col + 1):
            return False
        return True

    def print_board(self):
        for r in range(8):
            for c in range(8):
                print('|{}'.format(self.data[r][c]), end='')
            print("|")
