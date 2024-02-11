import tkinter as tk
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("400x150")  # Size of the window
my_w.title("www.plus2net.com")  # Adding a title
my_dict={'A':5,'B':4,'C':3,'D':3,'E':1,'F':0}
months=list(my_dict.keys()) # All keys are taken as options
font1=('Times',18,'normal')
def my_upd(*args):
    #l1.insert(0,'lsdhfs')
    #str1.set(sel.get()) #  Key name A B C D is displayed
    #str2.set(my_dict[sel.get()]) # value of the key is displayed
    print('sdsdsd')

sel=tk.StringVar() # string variable for the Combobox
cb1=ttk.Combobox(my_w,values=months,width=7,
    textvariable=sel,font=font1)
cb1.grid(row=1,column=1,padx=10, pady=20)
sel.set(months[0])
print(type(sel))
sel.trace('w', my_upd)

str1=tk.StringVar() # for entry1
str2=tk.StringVar() # for entry2

l1=tk.Entry(my_w,font=font1,width=5,textvariable=str1)
l1.grid(row=1,column=2,padx=5)

l2=tk.Entry(my_w,font=font1,width=5,textvariable=str2)
l2.grid(row=1,column=3,padx=5)


my_w.mainloop()  # Keep the window open