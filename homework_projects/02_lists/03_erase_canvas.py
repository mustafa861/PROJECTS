
import tkinter as tk

class EraserCanvas:

    def __init__(self, root, rows=10, cols=10, cell_size=50, eraser_size=80):

        self.root = root

        self.rows = rows

        self.cols = cols

        self.cell_size = cell_size

        self.eraser_size = eraser_size
        
        self.canvas = tk.Canvas(root, width=cols*cell_size, height=rows*cell_size, bg="white")

        self.canvas.pack()

        self.cells = {}  

        self.create_grid()
       
        self.eraser = self.canvas.create_rectangle(0, 0, eraser_size, eraser_size, fill="white", outline="black")
      
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def create_grid(self):

        for row in range(self.rows):
           
            for col in range(self.cols):
           
                x1, y1 = col * self.cell_size, row * self.cell_size
           
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
           
                cell_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
           
                self.cells[cell_id] = (x1, y1, x2, y2)

    def move_eraser(self, event):
       
        x1, y1 = event.x - self.eraser_size // 2, event.y - self.eraser_size // 2
       
        x2, y2 = x1 + self.eraser_size, y1 + self.eraser_size
     
        self.canvas.coords(self.eraser, x1, y1, x2, y2)

       
        for cell_id, (cx1, cy1, cx2, cy2) in self.cells.items():
            
            if self.overlaps(x1, y1, x2, y2, cx1, cy1, cx2, cy2):
            
                self.canvas.itemconfig(cell_id, fill="white")

    def overlaps(self, x1, y1, x2, y2, cx1, cy1, cx2, cy2):
        
        return not (x2 < cx1 or x1 > cx2 or y2 < cy1 or y1 > cy2)

if __name__ == "__main__":

    root = tk.Tk()

    root.title("Eraser Canvas")

    EraserCanvas(root)

    root.mainloop()
