import tkinter as tk
from gol import GOL
from brush import BaseBrush, GliderBrush, BlinkerBrush, PulsarBrush

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
        self.canvas.grid(row= 1, column=0, columnspan=4)
        self.canvas.bind("<Button-1>", self.toggle_cell)

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=0, column=0, columnspan=4)

        tk.Button(button_frame, text="Base", command=lambda: self.set_brush(BaseBrush())).grid(row= 0, column= 0)
        tk.Button(button_frame, text="Glider", command=lambda: self.set_brush(GliderBrush())).grid(row= 0, column= 1)
        tk.Button(button_frame, text="Blinker", command=lambda: self.set_brush(BlinkerBrush())).grid(row= 0, column= 2)
        tk.Button(button_frame, text="Pulsar", command=lambda: self.set_brush(PulsarBrush())).grid(row= 0, column= 3)

        self.draw_grid()

        button_frame2 = tk.Frame(self.root)
        button_frame2.grid(row=3, column=0, columnspan=4)

        self.step_button = tk.Button(button_frame2, text="Step", command=self.step)
        self.step_button.grid(row= 3, column= 1)
        self.start_button = tk.Button(button_frame2,text="Start",command=self.toggle_running)
        self.start_button.grid(row= 3, column= 0)

        self.is_running = False
        stats = self.game.get_statistics()
        self.info_label = tk.Label(self.root, text=f"Generation: {stats['generation']} | Alive: {stats['alive']} | Dead: {stats['dead']}")
        self.info_label.grid(row= 4, column= 0, columnspan=4)
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
                    outline="gray")
                

    def update_info(self):
        stats = self.game.get_statistics()
        self.info_label.config(text=f"Generation: {stats['generation']} | Alive: {stats['alive']} | Dead: {stats['dead']}")
    

    def set_brush(self, brush):
        self.brush = brush

if __name__ == "__main__":
    gol = GOL(GRID_WIDTH, GRID_HIGHT)
    GolGUI(gol)

