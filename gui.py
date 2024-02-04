#https://www.youtube.com/watch?v=2Z8qRJ7Lqag
import tkinter
import requests
from io import BytesIO
## В Linux установка PIL начинается с установки нескольких зависимых пакетов.
## В терминале выполните следующую команду для установки этих пакетов:
##    sudo apt-get install libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev
##Источник: https://uchet-jkh.ru/i/kak-ustanovit-pil-posagovaya-instrukciya
from PIL import Image, ImageTk

#tkinter.Tk.
def btncmd():
    ent.insert(tkinter.END, "!")
    print(ent.get())
    load_img()


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


myimg_png = tkinter.PhotoImage(file='imgPython.png') # only png!!!
l_logo = tkinter.Label(mywnd, image=myimg_png)
l_logo.pack()


ent = tkinter.Entry(mywnd)
ent.pack()
ent.insert(0, 'hello')
ent.insert(tkinter.END, ' World!')




l_urlPic = tkinter.Label(mywnd)
l_urlPic.pack()

pic_url = 'https://static.vecteezy.com/system/resources/previews/019/564/261/original/happy-chinese-new-year-2024-year-of-the-dragon-zodiac-vector.jpg'

def load_img():
    response = requests.get(pic_url)
    if response.status_code!=200:
        lbl['text'] = 'immage not found'
    else:
        img_from_url = ImageTk.PhotoImage(Image.open(BytesIO(response.content)).resize((100, 200), Image.LANCZOS))
        l_urlPic.config(image=img_from_url)
        l_urlPic.image = img_from_url


my_frame = tkinter.Frame(mywnd, bg='orange')
my_frame.pack()


mywnd.mainloop()