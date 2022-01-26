from tkinter import *
from MyModule import *

k=0
def klikker(event):
    global k
    k+=1
    nupp.config(text=k)
def klikker_(event):
    global k
    k-=1
    nupp.config(text=k)
def txt_to_lbl(event):
    t=txt.get()
    lbl.configure(text=t)
    txt.delete(0,END)
def valimine():
    valik=var.get()
    lbl.configure(text=valik)
    txt.insert(0,valik)


aken=Tk()
aken.title("Graf")
aken.geometry("800x500")

nupp=Button(aken,text="I am a button",font="Arial 20",width=20,bg="#FF6347",fg="#000080",relief=RAISED)
nupp.pack()#place(x=280,y=220)#side=LEFT
nupp.bind("<Button-1>",klikker)
nupp.bind("<Button-3>",klikker_)

lbl=Label(aken,text="Lol",height=3,width=20,font="Arial 20",fg="green",bg="lightblue",relief="solid")
lbl.pack()

txt=Entry(aken,width=20,font="Arial 20",fg="red",bg="lightblue",justify=CENTER)
txt.pack()
txt.bind("<Return>",txt_to_lbl)#enter

i1=PhotoImage(file="cat.png")
i2=PhotoImage(file="bob.png")
i3=PhotoImage(file="triangle.png")

var=StringVar()
var.set("Üks")
r1=Radiobutton(aken,image=i1,variable=var,value="Üks",command=valimine)
r2=Radiobutton(aken,image=i2,variable=var,value="Kaks",command=valimine)
r3=Radiobutton(aken,image=i3,variable=var,value="Kolm",command=valimine)
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)

aken.mainloop()
