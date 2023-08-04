from tkinter import *
import tkinter as tk
import tkinter.messagebox
import random
import customtkinter

# layout geral da aplicação
root = customtkinter.CTk()
root.title('Estou contrarado??')
largura = 400
altura = 400

largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

posX = largura_tela / 2 - largura / 2
posY = altura_tela / 2 - altura  / 2

root.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))
root._set_appearance_mode('System')
root.resizable(False,False)
root.configure(background='darkslategrey')

def houver(event):
    x = random.randint(0,200)
    y = random.randint(0,200)
    nao.place(x=x,y=y)

def onClick():
    tk.messagebox.showinfo("Confirmação","Você escolheu bem, não vai se arrepender!")


# título
pergunta = customtkinter.CTkLabel(root, text="Estou contratado?")
pergunta.pack(anchor='n', padx=20)
pergunta.place(x=130,y=40)


# configuração dos botões
nao = customtkinter.CTkButton(root, text="Não sei",text_color='white',fg_color="darkred")
nao.place(x=180, y=100)
nao.bind("<Enter>", houver)

sim = customtkinter.CTkButton(root, text="Quero sim",fg_color='darkslategrey',text_color='white', hover_color='green',command=onClick)
sim.place(x=50, y=100)

root.mainloop()