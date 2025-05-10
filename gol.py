class GOL:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.generations = 0
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.back_states = []
        
    def __str__(self):
        outstring = ""
        for rows in self.board:
            for cols in rows:
                outstring += str(cols) + " "
            outstring += "\n"
        return outstring
    
    def set_cell(self, row, col):
        if row >= 0 and row < self.rows and col >= 0 and col < self.cols:
            self.back_states.append(self.board)
            if len(self.back_states) > 5:
                self.back_states.pop(0)
            self.board[row][col] = (self.board[row][col] + 1) % 2
        
    def next_state(self):
        next_board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        direction = [(-1,-1), (-1,0), (-1,1),
                     (0,-1),          (0,1),
                     (1,-1),   (1,0), (1,1)]
        for r in range(self.rows):
            for c in range(self.cols):
                live_cells = 0
                for dr,dc in direction:
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nr < self.rows and nc >= 0 and nc < self.cols:
                        live_cells += self.board[nr][nc]
                # underpopulation
                if self.board[r][c] == 1 and live_cells < 2:
                    next_board[r][c] = 0
                # survival
                if self.board[r][c] == 1 and (live_cells == 2 or live_cells == 3):
                    next_board[r][c] = 1
                # overpopulation
                if self.board[r][c] == 1 and live_cells > 3:
                    next_board[r][c] = 0
                # reproduction
                if self.board[r][c] == 0 and live_cells == 3:
                    next_board[r][c] = 1
        self.back_states.append(self.board)
        if len(self.back_states) > 5:
            self.back_states.pop(0)
        self.board = next_board
        self.generations += 1

    def get_statistics(self):
        alive = sum([self.board[r][c] for r in range(self.rows) for c in range(self.cols)])
        dead = (self.rows * self.cols) - alive
        return {
                "alive"      : alive,
                "dead"       : dead,
                "generation" : self.generations
               }
    
    def back_step(self):
        self.board = self.back_states.pop()
        if self.generations > 0:
            self.generations -= 1

        


if __name__ == "__main__":
    gol = GOL(5,5)
    """
    print(gol.cols)
    print(gol.rows)
    print(gol.generations)
    print(gol)
    print(gol.get_statistics())
    gol.set_cell(2,1)
    gol.set_cell(2,2)
    gol.set_cell(2,3)
    print(gol)
    print(gol.get_statistics())
    gol.next_state()
    print(gol)
    print(gol.get_statistics())
    print(gol.generations)
    gol.next_state()
    print(gol)
    print(gol.get_statistics())
    gol.next_state()
    print(gol)
    print(gol.get_statistics())"""
    gol.set_cell(2,1)
    gol.set_cell(2,2)
    gol.set_cell(2,3)
    print(gol)
    gol.next_state()
    print(gol)
    gol.next_state()
    print(gol)
    gol.back_step()
    gol.back_step()
    print(gol)
