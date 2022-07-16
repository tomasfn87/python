from tkinter import Tk, Label, RAISED

root = Tk()
labels = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

for r in range(4):
    for c in range(3):
        label = Label(root, relief=RAISED, padx=25, pady=40, text=labels[r][c])
        label.grid(row=r, column=c)
root.mainloop()