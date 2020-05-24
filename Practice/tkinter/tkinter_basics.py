from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox as tkm

root = Tk()

fontStyle1 = tkFont.Font(family='Times New Roman', size=20)

# l1 = Label(root, text='Name', font=fontStyle1)
# l2 = Label(root, text='Password')
# entry1 = Entry(root)
# entry2 = Entry(root)

# l1.grid(row=0, sticky=E)
# l2.grid(row=1, sticky=E)

# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)

# l1.pack()
# l1.place(relx=0.45, rely=0.45, 
# 	relheight=0.1, relwidth=0.1)
# entry1.pack()
# entry1.place(anchor=NE)

# l2.pack(side=LEFT, expand=True)
# entry2.pack(side=RIGHT, expand=True)


def doNothing():
	print('Abcd')

def blah():
	tkm.showinfo('Blah!', 'Blah!')

def blah2():
	ans = tkm.askquestion('Question 1', 'Do you like Blah the religion?')
	if ans == 'yes':
		tkm.showinfo('Blah!', 'You have achieved comedy!')


menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label='File', menu=submenu)
submenu.add_command(label='New Project...', command=doNothing)
submenu.add_command(label='Save', command=doNothing)
submenu.add_separator()
submenu.add_command(label='Exit', command=root.quit)

editmenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Haha', command=doNothing)

## Toolbar ###

toolbar = Frame(root, bg='blue')
b1 = Button(toolbar, text='Insert image', command=blah)
b1.pack(side=LEFT, padx=10, pady=2)
b2 = Button(toolbar, text='Remove image', command=blah2)
b2.pack(side=LEFT, padx=10, pady=2)

toolbar.pack(side=TOP, fill=X)

### CNAVAS images ###

canvas = Canvas(root, width=200, height=100)
canvas.pack(pady=100)

blackline = canvas.create_line(0, 0, 200, 50)
redline = canvas.create_line(0, 100, 200, 50, fill='red')
box = canvas.create_rectangle(25, 25, 130, 60, fill='#fafa11')
# canvas.delete(redline)


### Status bar ###

status = Label(root, text='Blah!', bd=2, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop() 