import tkinter as tk
from gol import GOL
from brush import BaseBrush

CELL_SIZE = 20
GRID_WIDTH = 20
GRID_HIGHT = 20


class GolGUI:
    def __init__(self, gol: GOL):
        self.game = gol
        self.root = tk.Tk()
        self.root.title("Game of Life")
        self.brush = BaseBrush()
        self.canvas = tk.Canvas(self.root,
                                width=GRID_WIDTH * CELL_SIZE, 
                                height=GRID_HIGHT * CELL_SIZE, 
                                bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.toggle_cell)
        self.info_label = tk.Label(self.root, text="Generáció: 0 | Élő sejtek: 0")
        self.info_label.pack()
        self.draw_grid()
        self.start_button = tk.Button(self.root,text="Start",command=self.toggle_running)
        self.start_button.pack()
        self.is_running = False
        self.root.mainloop()
    
    def toggle_running(self):
        self.is_running = not self.is_running
        self.start_button.config(text="Pause" if self.is_running else "Start")
        if self.is_running:
            self.run()
    
    def run(self):
        if self.is_running:
            self.step()
            self.root.after(500,self.run)
    
    def step(self):
        self.game.next_state()
        self.draw_grid()
        self.update_info()

    def toggle_cell(self,event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        self.brush.apply(gol,row,col)
        self.draw_grid()
    
    def draw_grid(self):
        self.canvas.delete("all")
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                colour = "black" if self.game.board[r][c] == 1 else "white"
                self.canvas.create_rectangle(
                    c*CELL_SIZE,
                    r*CELL_SIZE,
                    (c+1)*CELL_SIZE,
                    (r+1)*CELL_SIZE,
                    fill=colour,
                    outline="gray"
                )


    def update_info(self):
        stats       = self.game.get_statistics()
        generation  = stats["generation"]
        alive_cells = stats["alive"]
        dead_cells  = stats["dead"]

        self.info_label.config(
            text=(
                f"Generáció: {generation}   "
                f"Élő sejtek: {alive_cells}   "
                f"Halott sejtek: {dead_cells}"))
            




if __name__ == "__main__":
    gol = GOL(GRID_WIDTH, GRID_HIGHT)
    GolGUI(gol)