from tkinter import *
from sympy import *

# configuracoes sympy
x,y,z = symbols('x y z')
init_printing(use_unicode = True)


def calcula_derivada():
    try:
        funcao = tx.get(1.0,END)
        printa(diff(funcao))
    except:
        res["text"] = "Syntax Error"
def calcula_integral():
    try:
        funcao1 = tx.get(1.0,END)
        printa(integrate(funcao1))
    except:
        res["text"] = "Syntax Error"
def limpar():
    tx.delete(1.0,END)

def printa(val):
    res["text"] = "Resultado = {}".format(val)
    
janela = Tk()
janela.title("Calculadora derivada integral")
janela.geometry("300x300+500+100")

# Frame principal
topFrame = Frame(janela)
topFrame.pack()

# Frame do texto
bottonFrame = Frame(janela)
bottonFrame.pack()

# Frame do botao
botton2Frame = Frame(janela)
botton2Frame.pack()

res = Label(janela, text = "Resultado = ...")
res.pack()

tx = Text(bottonFrame, height = 2,width = 150)
tx.pack()

bt1 = Button(botton2Frame,text = "Derivar", fg = "black", width = 10,command = calcula_derivada)
bt2 = Button(botton2Frame,text = "Integral",fg = "black", width = 10,command = calcula_integral)
bt3 = Button(botton2Frame,text = "Limpar",fg = "black", width = 10,command = limpar)

image = PhotoImage(file = "thumb nail thor brabo.png")
label = Label(janela,image = image)
label.pack()

bt1.pack(side = LEFT)
bt2.pack(side = LEFT)
bt3.pack(side = LEFT)
janela.mainloop()