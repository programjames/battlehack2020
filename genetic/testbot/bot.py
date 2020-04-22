def max(a, b):
    return a if a > b else b

def min(a, b):
    return a if a < b else b

def check_space_wrapper(r, c, board_size, team=Team.WHITE, opp_team=Team.BLACK):
    # check space, except doesn't hit you with game errors
    if r < 0 or c < 0 or c >= board_size or r >= board_size:
        return 0
    try:
        team_there = check_space(r, c)
        if team_there == False:
            return 0
        if team_there is team:
            return 1
        else:
            return -1
    except:
        return 0

CENTER_MULTIPLIER = -0.7907822902051973
DISTANCE_ENEMY_MULTIPLIER = 3.0911788574398384
DISTANCE_FRIENDLY_MULTIPLIER = -5.282679434855145
FINISHED_MULTIPLIER = 3.414835990920963
PAWNS_MULTIPLIER = 3.853422030726663
ODD_MULTIPLIER = -0.7069367969710008 * 5

def center(col, board_size):
    return abs(col - (board_size-1)/2)

def distance_enemy(board, col, board_size):
    for i in range(board_size):
        if board[i][col] == -1:
            return i
    return board_size

def distance_friendly(board, col, board_size):
    for i in range(board_size):
        if board[i][col] == 1:
            return i
    return board_size

def finished(board, col, board_size):
    return 1 if board[board_size-1][col] == 1 else 0

def odd(col):
    return col % 2

def pawns(board, col, board_size):
    if col == 0:
        s = 0
        for r in range(board_size):
            for c in (col, col+1):
                s += board[r][c]
        return s
    
    if col == board_size - 1:
        s = 0
        for r in range(board_size):
            for c in (col-1, col):
                s += board[r][c]
        return s

    s = 0
    for r in range(board_size):
        for c in (col-1, col, col+1):
            s += board[r][c]
    return s

def overlord_heuristic(board, col, board_size):
    h = 0
    h += CENTER_MULTIPLIER * center(col, board_size)
    h += DISTANCE_ENEMY_MULTIPLIER * distance_enemy(board, col, board_size)
    h += DISTANCE_FRIENDLY_MULTIPLIER * distance_friendly(board, col, board_size)
    h += FINISHED_MULTIPLIER * finished(board, col, board_size)
    h += ODD_MULTIPLIER * odd(col)
    h += PAWNS_MULTIPLIER * pawns(board, col, board_size)
    return h

def overlord_turn():
    board_size = get_board_size()
    team = get_team()
    opp_team = Team.WHITE if team == Team.BLACK else team.BLACK

    board = get_board()
    board = [[0 if not x else (1 if x == team else -1) for x in row] for row in board]
    if team == Team.WHITE:
        index = 0
    else:
        index = board_size - 1
        board = board[::-1]

    best_h = -100000
    best_col = None
    for col in range(board_size):
        if board[0][col] != 0:
            continue
        
        h = overlord_heuristic(board, col, board_size)
        if best_col is None or h < best_h:
            best_col = col
            best_h = h

    if best_col is not None:
        spawn(index, best_col)

class Pawn:
    def __init__(self):
        self.board_size = get_board_size()
        self.team = get_team()
        self.opp_team = Team.WHITE if self.team is Team.BLACK else Team.BLACK
        self.row, self.col = get_location()
        self.board = [[self.check_space(self.row+y, self.col+x) for x in range(-2, 3)] for y in range(-2, 3)]
        if self.team == Team.BLACK:
            self.board = self.board[::-1]
            self.row = self.board_size - 1 - self.row

    def check_space(self, row, col):
        if row < 0 or col < 0 or col >= self.board_size or row >= self.board_size:
            return 0
        try:
            team_there = check_space(row, col)
            if team_there is self.team:
                return 1
            elif team_there is self.opp_team:
                return -1
            return 0
        except:
            return 0

        
    def move_forward(self):
        move_forward()

    def capture(self, direction):
        # Capture a piece.  +1 = right, -1 = left
        if self.team == Team.WHITE:
            capture(self.row + 1, self.col + direction)
        else:
            capture(self.board_size - self.row - 2, self.col + direction)

    def cannot_move(self):
        return ((self.board[3][2] != 0 and
                 self.board[3][1] != -1 and
                 self.board[3][3] != -1) or
                self.row == self.board_size - 1)

    def empty_ahead(self):
        # Are there any enemy robots in front of us?
        for row in (3, 4):
            for col in (0, 1, 2, 3, 4):
                if self.board[row][col] == -1:
                    return False
        return True

    def get_threats(self):
        threats = [i for i in (-1, 1) if self.board[3][2+i] == -1]
        return threats

    def get_supporting(self):
        supporting = [i for i in (-1, 1) if self.board[3][2+i] == 1]
        return supporting

    def count_corner_enemies(self):
        return (1 if self.board[4][0] == -1 else 0) + (1 if self.board[4][4] == -1 else 0)

    def count_L_enemies(self):
        return (1 if self.board[4][1] == -1 else 0) + (1 if self.board[4][3] == -1 else 0)

    def get_L2_enemies(self):
        return [i for i in (-1, 1) if self.board[3][2+2*i] == -1]
    
    def count_side_enemies(self):
        return (1 if self.board[2][1] == -1 else 0) + (1 if self.board[2][3] == -1 else 0)

    def get_supports(self):
        return [i for i in (-1, 1) if self.board[1][2+i] == 1]
    
    def get_side_friends(self):
        side_friends = [i for i in (-1, 1) if self.board[2][2+2*i] == 1]
        return side_friends
    
    def must_support_corners(self):
        if self.board[4][0] == -1 and self.board[3][1] == 1:
            return True
        if self.board[4][4] == -1 and self.board[3][3] == 1:
            return True
        return False

    def get_neighbors(self):
        return [i for i in (-1, 1) if self.board[2][2+i] == 1]

    def back_filled(self):
        for row in (0, 1, 2):
            for col in (1, 2, 3):
                if self.board[row][col] != 1:
                    return False
        return True
    
    def do_turn(self):
        if self.cannot_move():
            return

        if self.must_support_corners():
            return
        
        threats = self.get_threats()
        if len(threats) > 0:                
            side_friends = self.get_side_friends()
            if len(threats) == 2:
                if len(side_friends) == 1:
                    self.capture(side_friends[0])
                    return
                self.capture(threats[0])
                return

            
            supports = self.get_supports()

            if len(supports) != 2 or threats[0] in side_friends or self.board[3][2] != -1:
                self.capture(threats[0])
                return
            
        if self.empty_ahead():
            self.move_forward()
            return

        side_enemies = self.count_side_enemies()
        if side_enemies == 1 and self.board[1][2] == 1:
            if (self.board[1][0] == 1 and self.board[2][1] == -1) or (self.board[1][4] == 1 and self.board[2][3] == -1):
                self.move_forward()
                return

        L_enemies = self.count_L_enemies()
        neighbors = self.get_neighbors()
        L2_enemies = self.get_L2_enemies()
        
        if L_enemies == 0:
            self.move_forward()
            return
        if L_enemies == 1 and len(neighbors) == 2 and len(L2_enemies) == 0:
            self.move_forward()
            return
        if L_enemies <= 2 and self.back_filled():
            self.move_forward()
            return

def pawn_turn():
    pawn = Pawn()
    pawn.do_turn()

def turn():
    robottype = get_type()
    if robottype == RobotType.PAWN:
        pawn_turn()
    else:
        overlord_turn()
