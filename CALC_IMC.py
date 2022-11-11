from tkinter import *
from tkinter import ttk
from tkinter import messagebox

###Cores###

co0 = "#444466"  # Preta/black
co1 = "#feffff"  # Branca/white
co2 = "#4065a1"  # Azul/blue

janela = Tk()
janela.title('')
janela.geometry('500x400')
janela.configure(bg=co1)

### Frames ###

frame_cima = Frame(janela, width=395, height=50, bg=co1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=395, height=280, bg=co1, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=2, column=0, sticky=NSEW)

style = ttk.Style(janela)
style.theme_use("clam")

### Frame Parte de Cima ###

app_nome = Label(frame_cima, text="CALCULAR SEU IMC", width=30, height=1, padx=0, relief='flat', anchor='center',
                 font=('Ivy 16 bold'), bg=co1, fg=co0)
app_nome.place(x=0, y=2)

app_linha = Label(frame_cima, text="", width=400, height=1, padx=0, relief='flat', anchor='nw', font=('Arial 1'),
                  bg=co2, fg=co1)
app_linha.place(x=0, y=35)


def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get())

    imc = peso / altura**2

    resultado = imc

    if resultado < 18.5:
        l_resultado_texto['text'] = "Abaixo do peso"

    elif resultado >= 18.5 and resultado < 25:
        l_resultado_texto['text'] = "Normal"

    elif resultado >= 25 and resultado < 30:
        l_resultado_texto['text'] = "Sobrepeso"
    else:
        l_resultado_texto['text'] = "Obesidade"

    l_resultado['text'] = "{:.{}f}".format(resultado, 2)


### Frame Parte de Baixo ###

l_nome = Label(frame_baixo, text='Nome do Paciente', height=1, padx=0, relief='flat', anchor='center',
               font=('Ivy 10 bold'), bg=co1, fg=co0)
l_nome.grid(row=0, column=0, columnspan=1, sticky=NW, pady=10, padx=3)
e_nome = Entry(frame_baixo, width=20, font=('Ivy 10 bold'), justify='center', relief=SOLID)
e_nome.grid(row=0, column=1, columnspan=1, sticky=NSEW, pady=10, padx=3)

l_email = Label(frame_baixo, text='Endereço Completo', height=1, padx=0, relief='flat', anchor='center',
               font=('Ivy 10 bold'), bg=co1, fg=co0)
l_email.grid(row=1, column=0, columnspan=1, sticky=NW, pady=10, padx=3)
e_email = Entry(frame_baixo, width=20, font=('Ivy 10 bold'), justify='center', relief=SOLID)
e_email.grid(row=1, column=1, columnspan=1, sticky=NSEW, pady=10, padx=3)

l_peso = Label(frame_baixo , text="Peso (Kg)", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_peso.grid(row=2, column=0, columnspan=1,  sticky=NW, pady=10, padx=3)
e_peso = Entry(frame_baixo, width=5, font=('Ivy 10 bold'),justify='center',relief=SOLID)
e_peso.grid(row=2, column=1, columnspan=1,  sticky=NSEW, pady=10, padx=3)

l_altura = Label(frame_baixo , text="Altura (cm)", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_altura.grid(row=3, column=0, columnspan=1,  sticky=NW, pady=10, padx=3)
e_altura = Entry(frame_baixo, width=5, font=('Ivy 10 bold'),justify='center',relief=SOLID)
e_altura.grid(row=3, column=1, columnspan=1,  sticky=NSEW, pady=10, padx=3)

l_resultado = Label(frame_baixo ,width=5, text="--------", height=1, padx=5, pady=80, relief="flat", anchor="center", font=('Ivy 24 bold'), bg=co2, fg=co1)
l_resultado.place(x=290, y=100)

l_resultado_texto = Label(frame_baixo , width=10, text="", height=1, padx=0, pady=8, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_resultado_texto.place(x=100, y=200)

b_calcular = Button(frame_baixo, command=calcular, text="Calcular",width=30, height=2, overrelief=SOLID,  bg=co2, fg="white", font=('Ivy 10 bold'), anchor="center", relief=RAISED )
b_calcular.grid(row=23, column=0,  sticky=NSEW, pady=1, padx=1, columnspan=12)


janela.mainloop()