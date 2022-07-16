from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM


root = Tk()
photo = PhotoImage(file='pato_donald.gif').subsample(2)
imagem = Label(master=root, image=photo)
imagem.pack(side=TOP)
texto = Label(master=root, font=('Courier', 18), text='HAAAAAAAAAAAAAAAAA!')
texto.pack(side=BOTTOM)
root.mainloop()
