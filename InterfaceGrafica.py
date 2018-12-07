from tkinter import *
from tkinter.ttk import Combobox
from Grafo import *

grafo = Grafo(dicGrafo, direcionado=True)

def bt_click():
    text_resultado_busca_em_largura.delete('1.0', END)
    text_resultado_busca_em_profundidade.delete('1.0', END)
    text_resultado_busca_com_A_estrela.delete('1.0', END)

    if combo1.get() in list(dicGrafo.keys()) and combo2.get() in list(dicGrafo.keys()):

        text_resultado_busca_em_largura.insert(END, grafo.busca_em_largura(combo1.get(), combo2.get()))
        text_resultado_busca_em_profundidade.insert(END, grafo.busca_profunda(combo1.get(), combo2.get()))
        text_resultado_busca_com_A_estrela.insert(END, grafo.busca_com_A_search(combo1.get(), combo2.get()))

        plota_largura(grafo_nx, combo1.get(), combo2.get())
        plota_profundidade(grafo_nx, combo1.get(), combo2.get())
        plota_A_estrela(grafo_nx, combo1.get(), combo2.get())

    else:
        popup = Tk()
        popup.title("Erro")
        message = Label(popup, text="Local não especificado no mapa.")
        message.place(x=20, y=20)
        bt_error = Button(popup, width=10, heigh=1, text="OK", command=popup.destroy)
        bt_error.place(x=70, y=55)
        popup.geometry("220x100+550+300")
        popup.mainloop()

janela = Tk()
janela.title("SmartSearch")

values = list(dicGrafo.keys())

lb_inicial = Label(janela, text="Local inicial:")
lb_inicial.place(x=20, y=20)

combo1 = Combobox(janela, values=values)
combo1.place(x=20, y=50)

lb_final = Label(janela, text="Local final:")
lb_final.place(x=200, y=20)

combo2 = Combobox(janela, values=values)
combo2.place(x=200, y=50)

label_busca_em_largura = Label(janela, text="Busca em largura:")
label_busca_em_largura.place(x=20, y=100)

text_resultado_busca_em_largura = Text(janela, width=100, height=3, relief=GROOVE, bg="white")
text_resultado_busca_em_largura.place(x=20, y=130)

label_busca_em_profundidade = Label(janela, text="Busca em profundidade:")
label_busca_em_profundidade.place(x=20, y=200)

text_resultado_busca_em_profundidade = Text(janela, width=100, height=3, relief=GROOVE, bg="white")
text_resultado_busca_em_profundidade.place(x=20, y=230)

label_busca_com_A_estrela = Label(janela, text="Busca com A*:")
label_busca_com_A_estrela.place(x=20, y=300)

text_resultado_busca_com_A_estrela = Text(janela, width=100, height=3, relief=GROOVE, bg="white")
text_resultado_busca_com_A_estrela.place(x=20, y=330)

bt1 = Button(janela, width=10, heigh=2, text="Confirmar", command=bt_click)
bt1.place(x=380, y=29)

janela.geometry("845x500+200+100")
janela.mainloop()