from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
import os


def new():
    global file
    root.title("Untitled -Notepad")
    file = None
    TextArea.delete(1.0, END)


def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " -Notepad")
            print("File Saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def openfile():
    global file
    if file == None:
        file = askopenfilename(defaultextension=".txt",
                                 filetypes=[("All files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            root.title(os.path.basename(file) + "-Notepad")
            TextArea.delete(1.0, END)
            f = open(file, "r")
            TextArea.insert(1.0, f.read())
            f.close()


def copy():
    TextArea.event_generate(("<<Copy>>"))



def cut():
    TextArea.event_generate(("<<Cut>>"))


def paste():
    TextArea.event_generate(("<<Paste>>"))

def Quit():
    root.destroy()


if __name__ == '__main__':
    root = Tk()
    root.geometry("700x600")
    root.title("Untitled -Notepad")

    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=new)
    filemenu.add_command(label="Save", command=save)
    filemenu.add_command(label="Open", command=openfile)
    filemenu.add_separator()
    filemenu.add_command(label="exit",command=Quit)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit" ,menu=editmenu)
    root.config(menu=menubar)
    scroll = Scrollbar(TextArea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)

    root.mainloop()
