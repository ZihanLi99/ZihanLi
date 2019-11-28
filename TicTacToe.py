class TicTacToe:
    def __init__(self) -> None:
        super().__init__()
        self.board = None
        self.current_state = None
        self.init()

    def init(self):
        self.board = [
            ['','',''],
            ['','',''],
            ['','',''],
        ]
        self.current_state = 'UNFINISHED'

    def get_current_state(self):
        return self.current_state

    def make_move(self, row, col, player):
        if 0<=row<=2 and 0<=col<=2 and self.board[row][col]== '' and self.current_state== 'UNFINISHED':
            self.board[row][col] = player
            self.check_status()
            return True
        return False

    def check_status(self):
        for r in range(3):
            if self.board[r][0]==self.board[r][1]==self.board[r][2] and self.board[r][0]!= '':
                if self.board[r][0]== 'x':
                    self.current_state= 'X_WON'
                else:
                    self.current_state= 'O_WON'
                return
        for c in range(3):
            if self.board[0][c]==self.board[1][c]==self.board[2][c] and self.board[0][c]!= '':
                if self.board[0][c]== 'x':
                    self.current_state= 'X_WON'
                else:
                    self.current_state= 'O_WON'
                return
        if self.board[0][0]==self.board[1][1]==self.board[2][2] and self.board[0][0]!= '':
            if self.board[0][0]== 'x':
                self.current_state= 'X_WON'
            else:
                self.current_state= 'O_WON'
            return
        if self.board[0][2]==self.board[1][1]==self.board[2][0] and self.board[1][1]!= '':
            if self.board[1][1]== 'x':
                self.current_state= 'X_WON'
            else:
                self.current_state= 'O_WON'
            return

        for r in range(3):
            for c in range(3):
                if self.board[r][c]== '':
                    self.current_state = 'UNFINISHED'
                    return
        self.current_state = 'DRAW'

    def print_board(self):
        for r in range(3):
            for c in range(3):
                print('{:1s}'.format(self.board[r][c]), end='')
            print()
