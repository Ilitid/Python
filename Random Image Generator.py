import tkinter
import random

OPTIONS_WIDTH = 500
OPTION_HEIGHT = 36

colors = ["#00FFFF", "#000000", "#0000FF", "#FF00FF",  # Aqua, Black, Blue, Fuchsia
          "#808080", "#008000", "#00FF00", "#800000",  # Gray, Green, Lime, Maroon
          "#000080", "#808000", "#800080", "#FF0000",  # Navy, Olive, Purple, Red
          "#C0C0C0", "#008080", "#FFFFFF", "#FFFF00"]  # Silver, Teal, White, Yellow
sizes = [[25, 15, 40, "[1]: big pixels, normal size"],
         [45, 25, 40, "[2]: big pixels, full screen"],
         [90, 50, 20, "[3]: normal pixels, full screen"],
         [90, 50, 10, "[4]: small pixels, normal size"],
         [920, 510, 2, "[5]: very small pixels, full screen (lags!)"]]


class Window:
    def __init__(self, title, width, height):
        self.root = tkinter.Tk()
        self.root.title(title)
        self.root.geometry("{0}x{1}+{2}+{2}".format(width, height, 5))
        self.root.resizable(False, False)
        self.canvas = tkinter.Canvas(self.root, width=width, height=height)
        self.canvas.pack()

# ----- options -----

options = Window("Chose image size", OPTIONS_WIDTH, OPTION_HEIGHT*len(sizes))


def click(event):
    global width, height, pixel_size
    clicked_row = event.y // OPTION_HEIGHT
    width = sizes[clicked_row][0]
    height = sizes[clicked_row][1]
    pixel_size = sizes[clicked_row][2]
    options.root.destroy()

options.root.bind("<Button-1>", click)

for i in range(len(sizes)):
    options.canvas.create_text(OPTIONS_WIDTH/2, OPTION_HEIGHT*(i+0.5), text=sizes[i][3], font="Arial 18")
    if i < len(sizes):
        options.canvas.create_line(0, (i+1)*OPTION_HEIGHT, OPTIONS_WIDTH, (i+1)*OPTION_HEIGHT)


options.root.mainloop()

# ----- image -----

image = Window("Random Image Generator", width*pixel_size, height*pixel_size)


def draw():
    image.canvas.delete("all")
    for row in range(height):
        for col in range(width):
            color = random.choice(colors)
            image.canvas.create_rectangle(pixel_size*col, pixel_size*row, pixel_size*(col+1),
                                          pixel_size*(row+1), fill=color, outline=color)

def crutch(event):
    draw()

image.root.bind("<Return>", crutch)
draw()

image.root.mainloop()
