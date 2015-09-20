try: from tkinter import *
except: from Tkinter import *
import runpy
from tictactoeminimax import Board

tac = Tk()
#Window Properties
tac.resizable(width=FALSE, height=FALSE)
tac.configure(background="#FFFFFF")
tac.geometry("300x390+450+100")
tac.title("One Player")
suk = IntVar()
ies = IntVar()
ies = 0
suk = 0
Tic = [1, 4, 7, 1, 7, 1, 2, 3]
Tac = [2, 5, 8, 5, 5, 4, 5, 6]
Toe = [3, 6, 9, 9, 3, 7, 8, 9]


def quit_win():

    tac.destroy()
    runpy.run_path("tictacmenu.py")

def computer():

    global b

    row, col = b.get_ai_move()
    b.move(row, col, "O")

    index = (col * 3) + row + 1

    moves[index] = "O"
    d[index].config(text="O", state=DISABLED, font="Arial 50", disabledforeground="black")
    return True

    # if moves[5] == "" and turn == 1:
    #     d[5].config(text="O", state=DISABLED, font="Arial 50", disabledforeground="black")
    #     moves[5] = "O"
    #     return
    # elif moves[5] == "X" and turn == 1:
    #     d[1].config(text="O", state=DISABLED, font="Arial 50", disabledforeground="black")
    #     moves[1] = "O"
    #     return
    # if turn > 1:
    #     global Tic
    #     global Tac
    #     global Toe
    #     for s, g, u in zip(Tic, Tac, Toe):
    #         if moves[s] == "O" and moves[g] == "O" and moves[u] == "":
    #             d[u].config(text="O", state=DISABLED, font="Arial 50", disabledforeground="black")
    #             moves[u] = "O"
    #             return


    #     for n, k, w in zip(Toe, Tac, Tic):
    #         if moves[n]=="O" and moves[k]=="O" and moves[w] == "":
    #             d[w].config(text="O", state=DISABLED, font="Arial 50", disabledforeground="black")
    #             moves[w] = "O"
    #             return


    #     for dr, mr, mrs in zip(Tic, Toe, Tac):
    #         if moves[dr]=="O" and moves[mr]=="O" and moves[mrs] == "":
    #             d[mrs].config(text="O", state=DISABLED, font="Arial 50", disabledforeground="black")
    #             moves[mrs] = "O"
    #             return

    #     for s, g, u in zip(Tic, Tac, Toe):

    #         if moves[s] == "X" and moves[g] == "X" and moves[u] == "":
    #             d[u].config(text="O", state=DISABLED, font="Arial 50", disabledforeground="black")
    #             moves[u] = "O"
    #             return

    #     for n, k, w in zip(Toe, Tac, Tic):

    #         if moves[n]=="X" and moves[k]=="X" and moves[w] == "":
    #             d[w].config(text="O", state=DISABLED, font="Arial 50", disabledforeground="black")
    #             moves[w] = "O"
    #             return

    #     for dr, mr, mrs in zip(Tic, Toe, Tac):

    #         if moves[dr]=="X" and moves[mr]=="X" and moves[mrs] == "":
    #             d[mrs].config(text="O", state=DISABLED, font="Arial 50", disabledforeground="black")
    #             moves[mrs] = "O"
    #             return

    #     if moves[2]=="" and moves[8]=="":
    #         d[2].config(text="O", state=DISABLED, font="Arial 50", disabledforeground="black")
    #         moves[2] = "O"
    #         return

    #     if moves[4]=="" and moves[6]=="":
    #         d[4].config(text="O", state=DISABLED, font="Arial 50", disabledforeground="black")
    #         moves[4] = "O"
    #         return
    #     if moves[3]=="" and moves[7]=="":
    #         if moves[8] == "X":
    #             d[7].config(text="O", state=DISABLED, font="Arial 50", disabledforeground="black")
    #             moves[7] = "O"
    #         else:
    #             d[3].config(text="O", state=DISABLED, font="Arial 50", disabledforeground="black")
    #             moves[3] = "O"
    #         return
    #     if moves[1]=="" and moves[9]=="":
    #         if moves[2] == "X":
    #             d[1].config(text="O", state=DISABLED, font="Arial 50", disabledforeground="black")
    #             moves[1] = "O"
    #         else:
    #             d[9].config(text="O", state=DISABLED, font="Arial 50", disabledforeground="black")
    #             moves[9]= "O"





def reset():
    global turn
    turn = 0
    global moves
    global b
    b = Board()
    moves = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
    for i in range(1,10):
        d[i].config(text="", state = NORMAL, bg = '#FF944D')

def click(x):
    global turn
    global b

    turn += 1
    d[x].config(text="X", state=DISABLED, font="Arial 50", disabledforeground="black")
    moves[x] = "X"
    row = int((x-1)/3)
    col = x % 3
    if col == 0:
        col = 2
    elif col == 1:
        col = 0
    elif col == 2:
        col = 1
    b.move(col, row, "X")

    computer()
    players = ["X", "O"]

    for o in players:
        global Tic
        global Tac
        global Toe

        for q, r, s in zip(Tic, Tac, Toe):

            if moves[q]==o and moves[r]==o and moves[s] == o:
                d[q].config(bg='green')
                d[r].config(bg='green')
                d[s].config(bg='green')
                global suk
                suk += 1
                comp.set("Computer: " + str(suk))


                for i in range(1,10):

                    d[i].config(state=DISABLED)
    count = 0
    for i in moves:
        if moves[i] != "":
            count+=1
    if count == 9:
        global ies
        ies += 1
        tys.set("Ties: " + str(ies))
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

    frame = Frame(tac, width=100, height=100)
    d[x] = Button(frame, text="", bg='#FF9448', command=lambda x=x: press(x))

    frame.grid_propagate(False)
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0,weight=1)
    frame.grid(row=i, column=p)
    d[x].grid(sticky='wens')

turn = 0
b = Board()
reset = Button(tac, command=reset, text="New Game").grid(row = 4, column = 2, pady= 10)
urscore = StringVar()
comp = StringVar()
tys = StringVar()


urscore.set("You: 0")
comp.set("Computer: " + str(suk))
tys.set("Ties: " + str(ies))


you_score = Label(tac, textvariable=urscore, bg="#FFFFFF").grid(row=0, column=1, pady=10)
ai_score = Label(tac, textvariable=comp, bg="#FFFFFF").grid(row=0, column=2)
ties = Label(tac, textvariable=tys, bg="#FFFFFF").grid(row=0, column=3)

tac.protocol("WM_DELETE_WINDOW", quit_win)


mainloop()
