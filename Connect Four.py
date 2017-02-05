import tkinter

# constants
WIDTH = 7
HEIGHT = 6
RADIUS = 50
DIAMETER = RADIUS * 2
TITLE = "Connect Four"
BG_COLOR = "#FFFFFF"
BOARD_COLOR = "#42AAFF"
YELLOW = "#FFFF00"
RED = "#FF0000"
BLACK = "#000000"

# variables
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=WIDTH*DIAMETER, height=HEIGHT*DIAMETER, bg=BOARD_COLOR)
game_over = True


# create field
def create_field():
    global field
    field = [[" " for x in range(WIDTH)] for x in range(HEIGHT)]


# draw a circle
def draw_circle(x, y, color, radius=RADIUS, tag=None):
    canvas.create_oval(x-radius, y-radius,
                       x+radius, y+radius,
                       fill=color, outline=color, tag=tag)


# make color transparent
def transparent(color):
    return color.replace('00', '7F')


# start/restart the game
def reset(event):
    global game_over, current_color
    create_field()
    canvas.delete("all")
    for row in range(HEIGHT):
        for column in range(WIDTH):
            draw_circle(DIAMETER*column+RADIUS, DIAMETER*row+RADIUS, BG_COLOR)
    current_color = YELLOW
    game_over = False


# clicking
def click(event):
    global game_over
    if game_over is False:
        global current_color
        clicked_column = event.x // DIAMETER
        for i in reversed(range(HEIGHT)):
            if field[i][clicked_column] == " ":
                draw_circle(clicked_column*DIAMETER+RADIUS, i*DIAMETER+RADIUS, current_color)
                field[i][clicked_column] = current_color
                if current_color == YELLOW:
                    current_color = RED
                else:
                    current_color = YELLOW
                break
        # check for victory
        # horizontal
        for row in field:
            for i in range(WIDTH-3):
                if row[i] == row[i + 1] == row[i + 2] == row[i + 3] != " ":
                    victory(row[i])
        # vertical
        for i in range(0, WIDTH):
            for b in range(0, HEIGHT-3):
                if field[b][i] == field[b + 1][i] == field[b + 2][i] == field[b + 3][i] != " ":
                    victory(field[b][i])
        # diagonal left to right
        for i in range(0, WIDTH-3):
            for b in range(0, HEIGHT-3):
                if field[b][i] == field[b + 1][i + 1] == field[b + 2][i + 2] == field[b + 3][i + 3] != " ":
                    victory(field[b][i])
        # diagonal right to left
        for i in range(3, WIDTH):
            for b in range(0, HEIGHT-3):
                if field[b][i] == field[b + 1][i - 1] == field[b + 2][i - 2] == field[b + 3][i - 3] != " ":
                    victory(field[b][i])
        # game over textbox
        if game_over:
            canvas.create_rectangle(DIAMETER*(WIDTH/2-2), DIAMETER*(HEIGHT/2-1),
                                    DIAMETER*(WIDTH/2+2), DIAMETER*(HEIGHT/2+1),
                                    fill=BG_COLOR, outline=BLACK)
            canvas.create_text(WIDTH*DIAMETER/2, HEIGHT*DIAMETER*0.45,
                               text="%s player won!" % winner, font="Arial 20")
            canvas.create_text(WIDTH*DIAMETER/2 , HEIGHT*DIAMETER*0.55,
                               text="Press Enter to restart", font="Arial 20")
            return
        # check for draw
        if field[0].count(" ") == 0:
            game_over = True
            canvas.create_rectangle(DIAMETER*(WIDTH/2-2), DIAMETER*(HEIGHT/2-1),
                                    DIAMETER*(WIDTH/2+2), DIAMETER*(HEIGHT/2+1),
                                    fill=BG_COLOR, outline=BLACK)
            canvas.create_text(WIDTH*DIAMETER/2, HEIGHT*DIAMETER*0.45,
                               text="It's a draw!", font="Arial 20")
            canvas.create_text(WIDTH*DIAMETER/2, HEIGHT*DIAMETER*0.55,
                               text="Press Enter to restart", font="Arial 20")


# a player has won
def victory(color):
    global game_over, winner
    game_over = True
    if color == YELLOW:
        winner = "Yellow"
    elif color == RED:
        winner = "Red"


# main
root.title(TITLE)
root.resizable(False, False)
canvas.pack()
canvas.create_text(WIDTH*DIAMETER/2, HEIGHT*DIAMETER*0.5,
                   text="Press Enter to Start/Restart the game", font="Arial 20")


# highlight column on hover
def highlight(event):
    if game_over is False:
        highlight_column = event.x // DIAMETER
        canvas.delete('highlight')
        for i in reversed(range(HEIGHT)):
            if field[i][highlight_column] == " ":
                draw_circle(highlight_column*DIAMETER+RADIUS, i*DIAMETER+RADIUS,
                            transparent(current_color), RADIUS-4, 'highlight')
                break


root.bind("<Button-1>", click)
root.bind("<Button-1>", highlight, "+")
root.bind("<Return>", reset)
root.bind("<Motion>", highlight)

root.mainloop()
