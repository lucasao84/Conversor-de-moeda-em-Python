from tkinter import *
from tkinter import Tk, Frame, Label
from PIL import Image, ImageTk
from tkinter import ttk

import requests
import json
import string

# Função converter

def converte():
    moeda_de = combo.get()
    moeda_para = combo2.get()
    valor_entrado = valor.get()
    response = requests.get('https://v6.exchangerate-api.com/v6/0e9c277f74593d7209f47368/latest/{}'. format(moeda_de))

    dados = json.loads(response.text)

    cambio = dados['conversion_rates'][moeda_para]

    resultado = float(valor_entrado) * float(cambio)

    if moeda_para == 'USD':
        simbolo = '$'
    elif moeda_para == 'EUR':
        simbolo = '€'
    elif moeda_para == 'AOA':
        simbolo = 'Kz'
    elif moeda_para == 'BRL':
        simbolo = 'R$'
    elif moeda_para == 'INR':
        simbolo = '₹'


    moeda_equivalente = simbolo + "{:,.2f}". format(resultado)
    app_resultado1['text'] = moeda_equivalente
    

# cores
cor0 = "#FFFFFF"  # white
cor1 = "#333333"  # black
cor2 = "#38576b"  # dark blue

janela = Tk()
janela.geometry('300x320')
janela.title("Conversor")
janela.configure(bg=cor0)

# Frame cima
frame_cima = Frame(janela, width=300, height=60, background=cor2)
frame_cima.grid(row=0, column=0)

# Frame baixo
frame_baixo = Frame(janela, width=300, height=260, background=cor0)
frame_baixo.grid(row=1, column=0, columnspan=2)

# Configurando Frame em cima
icon = Image.open('icon.png')
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)

app_imagem = Label(frame_cima, image=icon, compound='left', text='Conversor de moeda', height=5, pady=30, padx=15, relief="raised", anchor='center', font=('Arial 16 bold'), bg=cor2, fg=cor0)
app_imagem.place(x=0, y=0)

app_resultado1 = Label(frame_baixo, width=20, text='' ,height=3, relief='solid', fg=cor1, anchor='center', font=('Ivy 13 bold'))
app_resultado1.place(x=50, y=10)


# Moedas

moeda = ['AOA', 'BRL', 'EUR', 'INR', 'USD']


app_resultado = Label(frame_baixo, width=8, text='De' ,height=1, relief='flat',bg='white' ,fg=cor1, anchor='nw', font=('Ivy 10 bold'))
app_resultado.place(x=48, y=90)
combo = ttk.Combobox(frame_baixo, width=8, justify='center', font='Ivy 12 bold')
combo.place(x=50, y=115)
combo['values'] = (moeda)



app_resultado2 = Label(frame_baixo, width=8, text='Para' ,height=1, relief='flat',bg='white' ,fg=cor1, anchor='nw', font=('Ivy 10 bold'))
app_resultado2.place(x=158, y=90)
combo2 = ttk.Combobox(frame_baixo, width=8, justify='center', font='Ivy 12 bold')
combo2.place(x=158, y=115)
combo2['values'] = (moeda)

valor = Entry(frame_baixo, width=22, justify='center', font=('Ivy 12 bold'), relief=SOLID)
valor.place(x=50, y=155)

botao = Button(frame_baixo, width=24,text='Converter', justify='center', font=('Ivy 10 bold'), relief='raised', bg=cor2, fg=cor0, command=converte)
botao.place(x=50, y=205)



janela.mainloop()
