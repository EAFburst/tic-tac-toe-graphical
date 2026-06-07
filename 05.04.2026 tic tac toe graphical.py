from tkinter import *
from tkinter import messagebox
wind = Tk()
wind.geometry("300x300")
wind.title("Tic-Tac-Toe")

c = Canvas(width=300, height=250)
c.pack(anchor=S)

c.create_line(50,120,250,120,fill = "black")
c.create_line(50,180,250,180,fill = "black")
c.create_line(120,50,120,250,fill = "black")
c.create_line(180,50,180,250,fill = "black")
text = Label(text="To restart press Enter")
text.pack(anchor=N)

answers = [""] * 9
numbers = [1,2,3,4,5,6,7,8,9]
counter = 0
start=True
start = BooleanVar()

def draw(posx, posy, pos):
    global counter
    answers.pop(pos)
    if counter%2 == 0:
        answers.insert(pos, "o")
        c.create_oval(posx-20,  posy-20, posx+20, posy+20)
    else:
        answers.insert(pos, "x")
        c.create_line(posx-20, posy-20, posx+20, posy+20)
        c.create_line(posx+20, posy+20, posx-20, posy-20)
    counter += 1

def main(event):
    global pos
    x = event.x
    y = event.y
    posx = 0
    posy = 0
    if 50<x<120 and 50<y<120:
        pos=0
        posx=75
        posy=75
        draw(posx, posy, pos)
    elif 120<x<180 and 50<y<120:
        pos=1
        posx=145
        posy=75
        draw(posx, posy, pos)
    elif 180<x<250 and 50<y<120:
        pos=2
        posx=205
        posy=75
        draw(posx, posy, pos)
    elif 50<x<120 and 120<y<180:
        pos=3
        posx=75
        posy=145
        draw(posx, posy, pos)
    elif 120<x<180 and 120<y<180:
        pos=4
        posx=145
        posy=145
        draw(posx, posy, pos)
    elif 180<x<250 and 120<y<180:
        pos=5
        posx=205
        posy=145
        draw(posx, posy, pos)
    elif 50<x<120 and 180<y<250:
        pos=6
        posx=75
        posy=205
        draw(posx, posy, pos)
    elif 120<x<180 and 180<y<250:
        pos=7
        posx=145
        posy=205
        draw(posx, posy, pos)
    elif 180<x<250 and 180<y<250:
        pos=8
        posx=205
        posy=205
        draw(posx, posy, pos)
    if counter > 4:
        tmp = check_win(answers)
        if tmp:
            messagebox.showinfo("The end", tmp+" win")
            start = False
        elif counter == 9:
            messagebox.showinfo("The end", "draw")
            start = False
        
def check_win(answers):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if answers[each[0]] == answers[each[1]] == answers[each[2]]:
            return answers[each[0]]
    return False

def restart_game(event):
    c.delete("all")
    c.create_line(50,120,250,120,fill = "black")
    c.create_line(50,180,250,180,fill = "black")
    c.create_line(120,50,120,250,fill = "black")
    c.create_line(180,50,180,250,fill = "black")
    text.pack(anchor=N)


c.bind_all("<Button-1>", main)
c.bind_all("<Return>", restart_game)
