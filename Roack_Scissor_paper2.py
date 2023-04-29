from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title("My 1st Game")
root.geometry("400x350")

chrs = "RPS"

def rps(player1,player2):
    if (player1 == "R" and player2 == "P"):
        messagebox.showinfo("Result", " Computer Won")
    elif (player1 == "P" and player2 == "R"):
        
        messagebox.showinfo("Result", "You Won")
    elif (player1 == "P" and player2 == "S"):
        
        messagebox.showinfo("Result", "Computer Won")
    elif player1 == "S" and player2 == "P":
        
        messagebox.showinfo("Result", "You Won")
    elif player1 == "R" and player2 == "S":
        
        messagebox.showinfo("Result", "You Won")
    elif player1 == "S" and player2 == "R":
        
        messagebox.showinfo("Result", "Computer Won")
         
    elif player1 == player2:
        #print("Match tie")
        messagebox.showinfo("Result", "Match Tie")
    else:
        #print("nothing")
        messagebox.showinfor("Result","Nothing")
    

def rock():
    player1 = "R"
    player2 = random.choice(chrs)
    rps(player1,player2)
def scissor():
    player1 = "S"
    player2 = random.choice(chrs)
    rps(player1,player2)
    
def paper():
    player1 = "P"
    player2 = random.choice(chrs)
    rps(player1,player2)



rock_button = Button(root, text = "Rock   ", font=("Helvetica", 10),bg = "grey",command = rock)
rock_button.place(x = 150, y = 40)
scissor_button = Button(root, text = "Scissor",font=("Helvetica", 10), bg = "green",command = scissor)
scissor_button.place(x = 150, y = 80)
paper_button = Button(root, text = "Paper   ", font=("Helvetica", 10),bg = "red",command = paper)
paper_button.place(x = 150, y = 120)

root.mainloop()