from tkinter import *
from tkinter import ttk

def draw_grid(canvas, event=None):
    wid = canvas.winfo_width()
    hgt = canvas.winfo_width()

def main():
    algs = ["Dijkstra's", "A*"]

    window = Tk()
    window.title("Pathfinding Algorithms Visualization")
    window.maxsize(1000, 1000)
    window.config(bg="#FFFFFF")

    # initialize UI object
    UI_frame = Frame(window, width=900, height=300, bg="#FFFFFF")
    UI_frame.grid(row=0, column=0, padx=10, pady=5)

    # create canvas to make the grid
    can = Canvas(window, height=1000, width=1000, bg='white')
    can.pack(fill=BOTH, expand=True)
    can.bind('<Configure>', draw_grid)

    window.mainloop()


if __name__ == '__main__':
    main()
