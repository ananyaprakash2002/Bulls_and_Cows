import tkinter as tk
from tkinter import messagebox
import random

MAX_ATTEMPTS = 10
fields = {'Number', }
number = []
attempts = 0
bulls = 0
cows = 0
guess = []
entries = {}

def makenumber():
    number.clear()
    guess.clear()
    for i in range(0, 4):
        x = random.randrange(9)
        number.append(x)
    if len(number)>len(set(number)):
        makenumber()  
    #print("computer number: ",number)
   

def game_rules(entries):
    # game rules
    rule = """
    *Guess number should consist of a four digit number.
    *Bulls means correct number in the correct position.
    *Cows means correct number in the wrong position."""
    messagebox.showinfo("Game Rules", rule)


def makeform(root, fields):
    global entries
    for field in fields:
        root.geometry("300x200")
        row = tk.Frame(root)
        lab = tk.Label(row, width=10, text=field + ": ", anchor='w', fg="black", bg='#35ADE9')
        ent = tk.Entry(row)
        ent.insert(0, "")
        row.pack(side=tk.TOP,fill=tk.X,padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries[field] = ent
    return entries


def play_game(entries):
    global attempts
    r = str(entries['Number'].get())

    if attempts >= MAX_ATTEMPTS:
        messagebox.showinfo("Warning", """You have exceeded MAX allowed count of 10 rounds.You have LOST the game!!!\n
        Number that needed to be guessed: """ + str(number))
        entries['Number'].delete(0, "end")
        makenumber()
    else:
        attempts += 1
        validate(r)


def validate(guess_number):
    global guess
    global entries
    if len(str(guess_number)) == 4:
        for i in range(4):
            guess.append(int(guess_number[i]))
        print("guess: ", guess)

        global bulls
        global cows
        global number
        bulls = 0
        cows = 0
        for j in range(0, 4):
            if guess[j] == number[j]:
                bulls += 1
            if guess[j] in number and guess[j] != number[j]:
                cows += 1
        if bulls == 4:
            messagebox.showinfo("VICTORY", "You have WON the game,\n The number of attempts taken: "+str(attempts))
            number.clear()
            makenumber()
        elif bulls != 4:
            guess = []
            message = "Bulls=" + str(bulls) + " " + "Cows=" + str(cows)
            messagebox.showinfo("info", message)
            entries['Number'].delete(0, "end")

    else:
        messagebox.showinfo("ERROR", "input must be 4 digits")
        entries['Number'].delete(0, "end")


if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)

    # generate the number
    makenumber()
    b1 = tk.Button(root, text='Consider Input', command=(lambda e=ents: play_game(e)), bg='#6BC7FF', fg='black',
                   padx=10, pady=10)
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Game Rules', command=(lambda e=ents: game_rules(e)), bg='#59C0FF', fg='black', padx=10,
                   pady=10)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit, padx=10, bg='#1EAAFF', fg='black', pady=10)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.configure(bg='#ABDFFF')
    root.mainloop()
