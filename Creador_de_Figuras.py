from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1000x600")
root.title("Trabajando en el Canvas usando funciones")
canvas = Canvas(root,width=990,height=490,bg="white",highlightbackground="lightgray")

label = Label(root,text="Selecciona un Color")
fillcolour=["red","green","blue","black"]
colour_dropdown = ttk.Combobox(root,state="readonly",values=fillcolour,width=10)

startx = Label(root,text="Inicio X")

coordinates_values=[10,50,100,200,300,400,500,600,700,800,900]
d1 = ttk.Combobox(root,state="readonly",values=coordinates_values,width=10)

starty = Label(root,text="Inicio Y")

d2 = ttk.Combobox(root,state="readonly",values=coordinates_values,width=10)

endx = Label(root,text="Final X")

d3 = ttk.Combobox(root,state="readonly",values=coordinates_values,width=10)

endy = Label(root,text="Final Y")

d4 = ttk.Combobox(root,state="readonly",values=coordinates_values,width=10)




label.place(relx=0.6,rely=0.9,anchor=CENTER)
colour_dropdown.place(relx=0.8,rely=0.9,anchor=CENTER)
startx.place(relx=0.1,rely=0.85,anchor=CENTER)
endx.place(relx=0.5,rely=0.85,anchor=CENTER)
starty.place(relx=0.3,rely=0.85,anchor=CENTER)
endy.place(relx=0.7,rely=0.85,anchor=CENTER)
d1.place(relx=0.2,rely=0.85,anchor=CENTER)
d2.place(relx=0.4,rely=0.85,anchor=CENTER)
d3.place(relx=0.6,rely=0.85,anchor=CENTER)
d4.place(relx=0.8,rely=0.85,anchor=CENTER)
canvas.pack()
root.mainloop()