import turtle
import tkinter as tk

HEIGHT =300
WIDTH = 600


def Draw_Shape():
    sides = int(entry.get())
    size = 100
    color = "black"
    line_thickness = 3
    angle = (((sides-2)*180)/sides)
    turtle.fillcolor('red')
    turtle.begin_fill()
    for i in range(sides):
            turtle.forward(size)
            turtle.right(180-angle)
    turtle.end_fill()
    turtle.done()
            
#print(Draw_Shape(draw()))
root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = '#80c1ff',bd=5)
frame.place(relx = 0.5, rely = 0.1,relwidth=0.75,relheight=0.1, anchor = 'n')

entry_label = tk.Label(frame,text="Enter Number of Edges:")
entry_label.place(relheight = 1, relwidth = 0.65)
entry = tk.Entry(frame,font = 40)
entry.place(relx= 0.45,relheight =1,relwidth=0.35)

button = tk.Button(frame, text = "Draw Shapes",font = 40, command = Draw_Shape)
button.place(relx=0.7,relheight = 1,relwidth=0.3)

#lower_frame = tk.Frame(root,bg = '#80c1ff', bd=10)
#lower_frame.place(relx= 0.5, rely =0.25, relheight = 0.6, relwidth = 0.75, anchor = 'n')

#label = tk.Label(lower_frame)
#label.place(relheight = 1,relwidth=1)



root.mainloop()

