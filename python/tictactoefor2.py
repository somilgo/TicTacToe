try: from tkinter import *
except: from Tkinter import *
import runpy

tic = Tk()

#Window Properties
tic.resizable(width=FALSE, height=FALSE)
tic.configure(background="white")
tic.geometry("300x390+450+100")
tic.title("Two Player")

tys = StringVar()
xxscore = StringVar()
ooscore = StringVar()
k = IntVar()
j = IntVar()
j=0
k=0
ies = IntVar()
ies = 0
resetCount = 0

def quit_win():
    tic.destroy()
    runpy.run_path("tictacmenu.py")

def reset():
    global resetCount
    resetCount += 1
    global turn
    if resetCount % 2 == 1:
        turn = 1
        oscore.config(bg = "#FFE0CC")
        xscore.config(bg = "white")

    else:
        turn = 0
        xscore.config(bg = "#FFE0CC")
        oscore.config(bg = "white")
    global moves
    moves = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
    for i in range(1,10):
        d[i].config(text="", state = NORMAL, bg = '#FF944D')

def click(x):
    global turn
    turn += 1
    if turn % 2 != 0:
        d[x].config(text="X", state=DISABLED, font="Arial 50", disabledforeground = "black")
        moves[x] = "X"
        oscore.config(bg = "#FFE0CC")
        xscore.config(bg = "white")
    else:
        d[x].config(text="O", state=DISABLED, font="Arial 50", disabledforeground = "black")
        moves[x] = "O"
        xscore.config(bg = "#FFE0CC")
        oscore.config(bg = "white")

    players = ["X", "O"]
    Tic = [1, 4, 7, 1, 7, 1, 2, 3]
    Tac = [2, 5, 8, 5, 5, 4, 5, 6]
    Toe = [3, 6, 9, 9, 3, 7, 8, 9]
    for o in players:

        for q, r, s in zip(Tic, Tac, Toe):

            if moves[q]==o and moves[r]==o and moves[s] == o:
                d[q].config(bg='green')
                d[r].config(bg='green')
                d[s].config(bg='green')
                for i in range(1,10):

                    d[i].config(state=DISABLED)

                if o == "X":
                    global j
                    j += 1
                    xxscore.set("Player X: " + str(j))
                    xscore.config(bg = "white")
                    oscore.config(bg = "white")
                    return
                elif o == "O":
                    global k
                    k += 1
                    ooscore.set("Player O: " + str(k))
                    xscore.config(bg = "white")
                    oscore.config(bg = "white")
                    return
    count = 0
    for i in moves:
        if moves[i] != "":
            count+=1
    if count == 9:
        global ies
        ies += 1
        tys.set("Ties: " + str(ies))
        xscore.config(bg = "white")
        oscore.config(bg = "white")
        for i in range(1,10):
            d[i].config(state=DISABLED, bg="#FFE0C2")




press = lambda x: click(x)

#Making the Tic Tac Toe Squares as buttons.

r = [1, 2, 3, 1, 2, 3, 1, 2, 3]
c = [1, 1, 1, 2, 2, 2, 3, 3, 3]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = {}
moves = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}


for i, p, x in zip(r, c, x):

    frame = Frame(tic, width=100, height=100)
    d[x] = Button(frame, text="", bg='#FF9448', command=lambda x=x: press(x))

    frame.grid_propagate(False)
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0,weight=1)
    frame.grid(row=i, column=p)
    d[x].grid(sticky='wens')

turn = 0

reset = Button(tic, command=reset, text="New Game").grid(row = 4, column = 2, pady= 10)

tic.protocol("WM_DELETE_WINDOW", quit_win)



xxscore.set("Player X: " + str(j))
ooscore.set("Player O: " + str(k))
tys.set("Ties: " + str(ies))

xscore = Label(tic, textvariable=xxscore, bg="#FFE0CC")
xscore.grid(row=0, column=1, pady=10)
oscore = Label(tic, textvariable=ooscore, bg="#FFFFFF")
oscore.grid(row=0, column=3)
ties = Label(tic, textvariable=tys, bg="#FFFFFF").grid(row=0, column=2)



mainloop()
