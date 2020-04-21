def max(a, b):
    return a if a > b else b

def min(a, b):
    return a if a < b else b

class Overlord:
    def __init__(self):
        self.board_size = get_board_size()
        self.team = get_team()
        self.board = get_board()
        self.board = [[0 if not x else 1 if x == self.team else -1 for x in row] for row in self.board]
        if self.team == Team.BLACK:
            self.board = self.board[::-1]

    def spawn(self, col):
        if self.team == Team.WHITE:
            spawn(0, col)
        else:
            spawn(self.board_size - 1, col)

    def can_spawn(self, col):
        return self.board[0][col] == 0

    def count_pawns(self, bottom, left, top, right, team):
        # Count the number of pawns of type team in the square
        count = 0
        for row in range(max(0, bottom), min(top, self.board_size)):
            for col in range(max(0, left), min(right, self.board_size)):
                if self.board[row][col] == team:
                    count += 1
        return count

    def count_col(self, col, team=1):
        return self.count_pawns(0, col, self.board_size, col+1, team)

    def get_counts(self):
        counts = []
        for col in range(self.board_size):
            counts.append(self.count_col(1) - self.count_col(-1))
        return counts

    def get_boundary(self):
        # Identify the bounding line between our pawns and theirs
        my_boundary = []
        for col in range(self.board_size):
            for row in range(self.board_size)[::-1]:
                if self.board[row][col] == 1:
                    my_boundary.append(row)
                    break
            else:
                my_boundary.append(-1)
        
        enemy_boundary = []
        for col in range(self.board_size):
            for row in range(self.board_size):
                if self.board[row][col] == -1:
                    enemy_boundary.append(row)
                    break
            else:
                enemy_boundary.append(self.board_size)

        boundary = [(my_boundary[i] + enemy_boundary[i]) // 2 for i in range(self.board_size)]
        return boundary

    def identify_weak_spots(self):        
        weak_spots = {}

        for col in range(self.board_size):
            enemies = self.count_pawns(0, col-1, self.board_size, col+2, -1)
            friends = self.count_pawns(0, col-1, self.board_size, col+2, 1)
            if enemies >= friends + 3:
                weak_spots[col] = enemies - friends
        
        boundary = self.get_boundary()
        for col in range(self.board_size):
            nearby_enemies = self.count_pawns(boundary[col]+1, col-1, boundary[col]+4, col+2, -1)
            nearby_friends = self.count_pawns(boundary[col]-2, col-1, boundary[col]+1, col+2, 1)
            if nearby_enemies > nearby_friends + 1:
                weak_spots[col] = (nearby_enemies - nearby_friends) + 1000

        for col in range(self.board_size):
            if boundary[col] < 4:
                weak_spots[col] = -boundary[col] + 1000000

        return weak_spots
    
    def find_channels(self):
        starts = []
        ends = []
        for col in range(self.board_size):
            start = self.board_size
            count = 0
            for row in range(self.board_size):
                if self.board[row][col] == -1:
                    break
                if start == self.board_size and self.board[row][col] == 1:
                    start = row
                if start and self.board[row][col] != 1:
                    break
                if self.board[row][col] == 1:
                    count += 1
            starts.append(start)
            ends.append(start + count)

        channels = []
        for col in range(1, self.board_size - 1):
            if self.count_col(col, 1) > 3:
                continue
            max_start = max(starts[col-1], starts[col+1])
            min_end = min(ends[col-1], ends[col+1])
            if min_end - max_start >= 4:
                channels.append(col)
        return channels

    def do_turn(self):
        weak_spots = self.identify_weak_spots()
        if weak_spots:
            weak_spots = sorted(weak_spots.keys(), key=lambda key: weak_spots[key], reverse=True)
            for weak_spot in weak_spots:
                if self.can_spawn(weak_spot):
                    self.spawn(weak_spot)
                    return

        channels = self.find_channels()
        for channel in channels:
            if self.can_spawn(channel):
                self.spawn(channel)
                return

        counts = self.get_counts()

        min_count = self.board_size + 1
        min_col = None
        for col in range(0, self.board_size, 2):
            count = counts[col]
            if (min_col is None or count < min_count) and self.can_spawn(col) and not self.is_finished(col):
                min_col = col
                min_count = count

        if min_col is not None:
            self.spawn(min_col)
            return

        min_count = self.board_size + 1
        min_col = None
        for col in range(1, self.board_size, 2):
            count = counts[col]
            if (min_col is None or count < min_count) and self.can_spawn(col) and not self.is_finished(col):
                min_col = col
                min_count = count

        if min_col is not None:
            self.spawn(min_col)
            return

        for col in range(self.board_size):
            if self.can_spawn(col):
                self.spawn(col)
                return

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
        threats = []
        if self.board[3][1] == -1:
            threats.append(-1)
        if self.board[3][3] == -1:
            threats.append(1)
        return threats

    def count_corner_enemies(self):
        return (1 if self.board[4][0] == -1 else 0) + (1 if self.board[4][4] == -1 else 0)

    def count_L_enemies(self):
        return (1 if self.board[4][1] == -1 else 0) + (1 if self.board[4][3] == -1 else 0)

    def must_support_corners(self):
        if self.board[4][0] == -1 and self.board[3][1] == 1:
            return True
        if self.board[4][4] == -1 and self.board[3][3] == 1:
            return True
        return False

    def neighbors_filled(self):
        return self.board[2][1] == 1 and self.board[2][3] == 1

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
            self.capture(threats[0])
            return

        if self.empty_ahead():
            self.move_forward()
            return

        L_enemies = self.count_L_enemies()
        if L_enemies == 0:
            self.move_forward()
            return
        if L_enemies == 1 and self.neighbors_filled():
            self.move_forward()
            return
        if L_enemies == 2 and self.back_filled():
            self.move_forward()
            return    

def overlord_turn():
    overlord = Overlord()
    overlord.do_turn()

def pawn_turn():
    pawn = Pawn()
    pawn.do_turn()

def turn():
    robottype = get_type()
    if robottype == RobotType.PAWN:
        pawn_turn()
    else:
        overlord_turn()
