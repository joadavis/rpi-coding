# /bin/python3

# a connecting game for Elias
# based on his crazy ideas for power ups

class GameBoard(object):
    num_rows = 6;
    num_columns = 7;
    gravity = True;
    wraparound = False;

    powerup_shield = False;
    powerup_X = False;
    powerup_bombs = False;

    board = []

    def __init__(self):
        # go by columns then rows
        # things get dropped from the top, right? so select a column and drop
        self.board = [[0 for cell in range(self.num_rows)] for col in range(self.num_columns)]


    def display(self):
        header = ""
        for x in range(self.num_columns):
            header+="+-"
        print(header + "+")
        #print(self.board)
        for rown in range(self.num_rows):
            row_str = " "
            for coln in range(self.num_columns):
                #row_str +=  self.board[coln][rown]
                row_str += f"{self.board[coln][rown]} "
            print(row_str)
        print(header + "+")

    def drop_in(self, col, chip):
        """ drop in the top of a column, falling down to the first empty spot"""
        # TODO: antigravity
        # TODO: bombs
        if (self.board[col][0] != 0):
            raise(Exception("no space!"))
        for rown in range(1, self.num_rows):
            if self.board[col][rown] != 0:
                self.board[col][rown - 1] = chip
                return
        self.board[col][self.num_rows - 1] = chip

    def check_for_winner(self):
        """ horiz, vert, diag from top left, other diag"""
        # horiz
        for rown in range(self.num_rows):
            last_seen = 0
            last_seen_count = 0
            for coln in range(self.num_columns):
                if self.board[coln][rown] == 0:
                    last_seen = 0
                    last_seen_count = 0
                elif self.board[coln][rown] == last_seen:
                    last_seen_count += 1
                    if last_seen_count == 4:
                        # todo try an f string
                        return(f"Player {last_seen} wins!")
                else:
                    last_seen = self.board[coln][rown]
                    last_seen_count = 1
        # vert
        for coln in range(self.num_columns):
            last_seen = 0
            last_seen_count = 0
            for rown in range(self.num_rows):
                if self.board[coln][rown] == 0:
                    last_seen = 0
                    last_seen_count = 0
                elif self.board[coln][rown] == last_seen:
                    last_seen_count += 1
                    if last_seen_count == 4:
                        # todo try an f string
                        return(f"Player {last_seen} wins!")
                else:
                    last_seen = self.board[coln][rown]
                    last_seen_count = 1            

        # from left top
        # reduce the search cycles, but each stop check all 4 cells
        for coln in range(self.num_columns - 3):
            for rown in range(self.num_rows - 3):
                cell = self.board[coln][rown]
                if cell != 0:
                    if cell == self.board[coln + 1][rown + 1] and \
                       cell == self.board[coln + 2][rown + 2] and \
                       cell == self.board[coln + 3][rown + 3]:
                           return(f"Player {cell} wins!!")

        # other diag
        for coln in range(3, self.num_columns):
            for rown in range(self.num_rows - 3):
                cell = self.board[coln][rown]
                if cell != 0:
                    if cell == self.board[coln - 1][rown + 1] and \
                       cell == self.board[coln - 2][rown + 2] and \
                       cell == self.board[coln - 3][rown + 3]:
                           return(f"Player {cell} wins!!")
        return(None) #no winner

    def list_open_columns(self):
        """ return a list of column number that are ok """
        open_columns = []
        for coln in range (self.num_columns):
            # not accounting for antigravity yet
            if self.board[coln][0] == 0:
                open_columns.append(coln)
        return(open_columns)


def test_case_1():
    gb = GameBoard()
    gb.display()
    print(gb.list_open_columns())
    gb.drop_in(3, 1)
    gb.drop_in(3, 2)
    gb.drop_in(4, 1)
    gb.display()
    print(gb.check_for_winner())
    gb.drop_in(3, 1)
    gb.drop_in(3, 1)
    gb.drop_in(3, 1)
    gb.drop_in(3, 1)
    print(gb.list_open_columns())
    gb.display()
    print(gb.check_for_winner())
    # this should fail
    gb.drop_in(3, 1)
    gb.drop_in(3, 1)
    gb.drop_in(3, 1)

def test_case_2_diag_tlbr():
    # from top left to bottom right
    gb = GameBoard()
    # fill in some spaces
    gb.drop_in(1, 1)
    gb.drop_in(1, 1)
    gb.drop_in(1, 1)
    gb.drop_in(2, 1)
    gb.drop_in(2, 1)
    gb.drop_in(3, 1)
    gb.display()
    print(gb.check_for_winner())
    gb.drop_in(1, 2)
    gb.drop_in(2, 2)
    gb.drop_in(3, 2)
    gb.display()
    print(gb.check_for_winner())
    gb.drop_in(4, 2)
    gb.display()
    check_result = gb.check_for_winner()
    if check_result == None:
        raise Exception("Should have had 2 as winner")
    print(check_result)

def test_case_3_diag_trbl():
    # from top right to bottom left
    gb = GameBoard()
    # fill in some spaces
    gb.drop_in(1, 1)
    gb.drop_in(2, 1)
    gb.drop_in(2, 1)
    gb.drop_in(3, 1)
    gb.drop_in(3, 1)
    gb.drop_in(3, 1)
    gb.display()
    print(gb.check_for_winner())
    gb.drop_in(1, 2)
    gb.drop_in(2, 2)
    gb.drop_in(3, 2)
    gb.display()
    print(gb.check_for_winner())
    gb.drop_in(0, 2)
    gb.display()
    check_result = gb.check_for_winner()
    if check_result == None:
        raise Exception("Should have had 2 as winner")
    print(check_result)


def game_loop():
    gb = GameBoard()
    noone_has_won = True
    while noone_has_won:
        # TODO show valid columns
        gb.display()
        # TODO get input for player 1
        # TODO call drop
        # check for winner
        # TODO repeat for player 2


if __name__ == '__main__':
    try:
        test_case_1()
    except Exception as ex:
        print(f"Expected something like {ex}")
    test_case_2_diag_tlbr()
    test_case_3_diag_trbl()
