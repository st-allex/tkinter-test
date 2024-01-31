#https://www.youtube.com/watch?v=2Z8qRJ7Lqag
import tkinter

def btncmd():
    ent.insert(tkinter.END, "!")
    print(ent.get())


mywnd = tkinter.Tk()

mywnd.geometry("600x900")
mywnd.resizable(width=False, height=False)
mywnd.title("my window")
#mywnd.iconbitmap("my.icon")
#mywnd.config(bg='black')
mywnd['bg'] = 'black'


btn = tkinter.Button(mywnd,
                     text='my btn',
                     width=10,
                     height=5,
                     bg='green',
                     activebackground='lime',
                     font=('DejaVu Serif Condensed', 20, 'italic'),
                     foreground='red',
                     activeforeground='yellow',
                     command=btncmd)
btn.pack()


lbl = tkinter.Label(mywnd,
                     text='my lbl',
                     width=10,
                     height=5,
                     bg='green',
                     font=('DejaVu Serif Condensed', 20, 'italic'),
                     foreground='red')
lbl.place(x=10, y=20)


myimg = tkinter.PhotoImage(file='imgPython.png') # only png!!!
l_logo = tkinter.Label(mywnd, image=myimg)
l_logo.pack()


ent = tkinter.Entry(mywnd)
ent.pack()
ent.insert(0, 'hello')
ent.insert(tkinter.END, ' World!')

###https://www.youtube.com/watch?v=w-GT7FmwGfI&list=PL9aGGxgLOVw5oEXMk8Qhg3RVWY2dtyw8H&index=9

mywnd.mainloop()