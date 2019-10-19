from tkinter import filedialog
from tkinter import *
import subprocess

lentry = 1

def txtprint(output):
    global lentry
    try:
        output = output.decode()
        output = output.strip()
    except AttributeError:
        pass
    if output in '':
        pass
    else:
        txt.configure(state='normal')
        txt.insert(0.0, '[' + str(lentry) + ']: ' + output.replace('\n', ' | ') + '\n')
        txt.configure(state='disabled')
        lentry += 1

def dirchoose():
    global repopath
    repopath = filedialog.askdirectory()
    txtprint(repopath)


def commit():
    try:
        a = subprocess.Popen("git add *", cwd=str(repopath), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        txtprint(a.stdout.read())
    except OSError:
        txtprint("[ADD] Invalid repository directory")

    try:
        b = subprocess.Popen("git commit -m " + '"' + e1.get() + '"', cwd=str(repopath), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        txtprint(b.stdout.read())
    except OSError:
        txtprint("[COMMIT] Invalid repository directory")

def erase(self):
    e1.delete(0, 'end')


def push():
    try:
        c = subprocess.Popen('git push origin master', cwd=str(repopath), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        txtprint(c.stdout.read())
    except OSError:
        txtprint("[PUSH] Invalid repository directory")


root = Tk()
root.title("Git Automater")
root.geometry("662x548")
root.resizable(False, False)
repopath = StringVar()

btn = Button(text="Choose Repository Folder", command=dirchoose)
f1 = Frame(root)
e1 = Entry(f1, text="Commit message...")
btn2 = Button(f1, text="Commit", command=commit)
btn3 = Button(text="Push", command=push)
txt = Text(width=80, height=30, wrap=NONE)
vscroll = Scrollbar(command=txt.yview)
hscroll = Scrollbar(command=txt.xview, orient=HORIZONTAL)

btn.grid(row=0, column=0, padx=10, pady=10)
e1.insert('end', "Commit message...")
e1.bind("<Button-1>", erase)
f1.grid(row=0, column=1)
e1.grid(row=0, column=0, padx=3)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
txt['yscrollcommand'] = vscroll.set
txt['xscrollcommand'] = hscroll.set
txt.grid(row=1, columnspan=3)
vscroll.grid(row=1, column=3, sticky='ns')
hscroll.grid(row=2, columnspan=3, sticky='ew')

root.mainloop()
