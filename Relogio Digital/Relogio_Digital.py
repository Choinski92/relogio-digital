from email.utils import collapse_rfc2231_value
from tkinter import *
import tkinter
from turtle import width, window_width
from datetime import datetime
from xmlrpc.client import DateTime
import pyglet

pyglet.font.add_file("digital-7.ttf")

#colores picker
cor1 = "#0a0a0a" #preto
cor2 = "#670469" #roxo

fundo = cor1
cor = cor2

#Janelas
janela = Tk()
janela.title("")
janela.geometry("415x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure (bg=cor1)

#relogio
def relogio():

    tempo=datetime.now()

    hora=tempo.strftime("%H:%M:%S")
    dia_semana=tempo.strftime("%A")
    dia=tempo.day
    mes=tempo.strftime("%B")
    ano=tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200,relogio)
    l2.config(text=dia_semana +" " + str(dia) + "/" + str(mes) + "/" + str(ano))

l1=Label(janela,text="", font=("digital-7 100"),bg=fundo,fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2=Label(janela,text="", font=("digital-7 26"),bg=fundo,fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)
relogio()

janela.mainloop()