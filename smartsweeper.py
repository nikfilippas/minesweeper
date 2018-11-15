"""
https://www.youtube.com/watch?v=LFU5ZlrR21E
"""

import tkinter as tk

master = tk.Tk()

cell_width = 15
cell_height = 15

#class grid():
#    def __init__(self, cell_width, cell_height):
#        self.cell_width = cell_width
#        self.cell_height = cell_height
#        
#        self.master = Tk()
#
#        self.canvas_width = 10*self.cell_width
#        self.canvas_height = 10*self.cell_height
#        
#        self.w = Canvas(self.master,
#                   width=self.canvas_width,
#                   height=self.canvas_height)
#        self.w.pack()
#        self.w.create_rectangle(50, 20, 150, 80, fill="green")
#
#        self.w.mainloop()


canvas_width = 10*cell_width
canvas_height = 10*cell_height

w = tk.Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()


#def create_grid():
#    """
#    """
#    
#    
#    
#    return None


def round_rectangle(canvas, x1, y1, x2, y2, radius=10, **kwargs):
    """
    Draws a rectangle with rounded corners.
    """    
    points = [x1+radius, y1,  x1+radius, y1,
              x2-radius, y1,  x2-radius, y1,
              x2, y1,
              x2, y1+radius,  x2, y1+radius,
              x2, y2-radius,  x2, y2-radius,
              x2, y2,
              x2-radius, y2,  x2-radius, y2,
              x1+radius, y2,  x1+radius, y2,
              x1, y2,
              x1, y2-radius,  x1, y2-radius,
              x1, y1+radius,  x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)


def draw_mine(size, pressed=False):
    """
    """
    if not pressed:
        color = "black"
        background = "#A9A9A9"
    else:
        color = "#800000"
        background = "#D3D3D3"
        
    master = tk.Tk()
    canvas = tk.Canvas(master, width=size, height=size)
    canvas.pack()
    
    # scaled coordinates
    W = size/150 * 15
    P = [size/150 * 5,    # [0]
         size/150 * 25,   # [1]
         size/150 * 50,   # [2]
         size/150 * 72,   # [3]
         size/150 * 75,   # [4]
         size/150 * 125,  # [5]
         size/150 * 145]  # [6]
    
    round_rectangle(canvas, 0, 0, size, size, width=W, fill=background)
    
    canvas.create_line(P[4], P[0], P[4], P[6], width=W, fill=color, arrow=tk.BOTH)
    canvas.create_line(P[0], P[4], P[6], P[4], width=W, fill=color, arrow=tk.BOTH)
    canvas.create_line(P[1], P[1], P[5], P[5], width=W, fill=color, arrow=tk.BOTH)
    canvas.create_line(P[1], P[5], P[5], P[1], width=W, fill=color, arrow=tk.BOTH)
    
    canvas.create_oval(P[1], P[1], P[5], P[5], fill=color, width=0)
    canvas.create_oval(P[2], P[2], P[3], P[3], fill="white", width=0)
    
    canvas.mainloop()

def CreateCell():
    return

    

#def callback():
#    return draw_mine

#f = tk.Frame(master, height=50, width=50)
#f.pack_propagate(0) # don't shrink
#f.pack()
#
#b = tk.Button(f, text="Sure!")
#b.pack(fill=tk.BOTH, expand=1)
#b.mainloop()

def create_grid():
    root = tk.Tk()
    tk.Grid.rowconfigure(root, 0, weight=1)
    tk.Grid.columnconfigure(root, 0, weight=1)
    
    #Create & Configure frame 
    frame=tk.Frame(root)
    frame.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    
    #Create a 5x10 (rows x columns) grid of buttons inside the frame
    for row_index in range(5):
        tk.Grid.rowconfigure(frame, row_index, weight=1)
        for col_index in range(10):
            tk.Grid.columnconfigure(frame, col_index, weight=1)
            btn = tk.Button(frame, text="0") #create a button inside frame 
            btn.grid(row=row_index, column=col_index, sticky=tk.N+tk.S+tk.E+tk.W)  
    
    root.mainloop()
    

def keep_flat(event):
    if event.widget is btn:
        event.widget.config(relief=tk.FLAT)


def callback(event):
    print("clicked at", event.x, event.y)

frame = tk.Frame(w, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

w.mainloop()
