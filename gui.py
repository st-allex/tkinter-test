import tkinter

def btncmd():
    print('hello')


mywnd = tkinter.Tk()

mywnd.geometry("600x600")
mywnd.resizable(width=False, height=False)
mywnd.title("my window")
#mywnd.iconbitmap("my.icon")
#mywnd.config(bg='black')
mywnd['bg'] = 'black'

btn = tkinter.Button(mywnd, text='my btn', command=btncmd)
btn.pack()

mywnd.mainloop()