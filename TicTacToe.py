class TicTacToe:
    def __init__(self):
        self._board = None
        self._current_state = None

    def init(self):
        self._board = [
            ['','',''],
            ['','',''],
            ['','',''],
        ]
        self._current_state = 'UNFINISHED'

    def get_current_state(self):
        return self._current_state

    def make_move(self, row, col, player):
        if 0 <= row <= 2 and 0 <= col <= 2 and self._board[row][col] =='' and self._current_state =='UNFINISHED':
            self._board[row][col] = player
            self.check_status()
            return True
        return False

    def check_status(self):
        for r in range(3):
            if self._board[r][0]==self._board[r][1]==self._board[r][2] and self._board[r][0]!='':
                if self._board[r][0]=='x':
                    self._current_state='X_WON'
                else:
                    self._current_state='O_WON'
                return
        for c in range(3):
            if self._board[0][c]==self._board[1][c]==self._board[2][c] and self._board[0][c]!='':
                if self._board[0][c]=='x':
                    self._current_state='X_WON'
                else:
                    self._current_state='O_WON'
                return
        if self._board[0][0]==self._board[1][1]==self._board[2][2] and self._board[0][0]!='':
            if self._board[0][0]=='x':
                self._current_state='X_WON'
            else:
                self._current_state='O_WON'
            return
        if self._board[0][2]==self._board[1][1]==self._board[2][0] and self._board[1][1]!='':
            if self._board[1][1]=='x':
                self._current_state='X_WON'
            else:
                self._current_state='O_WON'
            return

        for r in range(3):
            for c in range(3):
                if self._board[r][c]=='':
                    self._current_state = 'UNFINISHED'
                    return
        self._current_state = 'DRAW'

    def print_board(self):
        for r in range(3):
            for c in range(3):
                print('{:1s}'.format(self._board[r][c]), end='')
            print()
