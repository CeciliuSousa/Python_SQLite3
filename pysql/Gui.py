from tkinter import *

class Gui():
    '''Classe da Interface Gráfica'''
    x = 5
    y = 3
    width_entry = 30

    window = Tk()
    window.wm_title("PYSQL versão 1.0")

    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCpf = StringVar()

    lblnome = Label(window, text="Nome")
    lblsobrenome = Label(window, text="Sobrenome")
    lblemail = Label(window, text="E-mail")
    lblcpf = Label(window, text="cpf")

    #Criando os objetos que farão parte das janelas
    entNome = Entry(window, textvariable=txtNome, width=width_entry)
    entSobrenome = Entry(window, textvariable=txtSobrenome, width=width_entry)
    entEmail = Entry(window, textvariable=txtEmail, width=width_entry)
    entCpf = Entry(window, textvariable=txtCpf, width=width_entry)

    listClientes = Listbox(window, width=100)
    scrollClientes = Scrollbar(window)
    btnViewAll = Button(window, text="Ver todos")
    btnBuscar = Button(window, text="Buscar")
    btnInserir = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Atualizar selecionados")
    btnDel = Button(window, text="Deletar selecionados")
    btnClose = Button(window, text="fechar")

    #Associando Objetos
    lblnome.grid(row=0, columns=0)
    lblsobrenome.grid(row=1, columns=0)
    lblemail.grid(row=2, columns=0)
    lblcpf.grid(row=3, columns=0)

    entNome.grid(row=0, columns=1, padx=50, pady=50)
    entSobrenome.grid(row=1, columns=1)
    entEmail.grid(row=2, columns=1)
    entCpf.grid(row=3, columns=1)

    listClientes.grid(row=0, columns=2, rowspan=10)
    scrollClientes.grid(row=0, columns=6, rowspan=10)
    btnViewAll.grid(row=4, columns=0, columnspan=2)
    btnBuscar.grid(row=5, columns=1, columnspan=2)
    btnInserir.grid(row=6, columns=1, columnspan=2)
    btnUpdate.grid(row=7, columns=1, columnspan=2)
    btnDel.grid(row=8, columns=1, columnspan=2)
    btnClose.grid(row=9, columns=1, columnspan=2)

    #Conectando o Scrollbar com ListBox
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    #Adicionar SWAG (aparência) à interface
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x, pady=y)
        elif widget_class == "ListBox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x, pady=y, sticky='N')

    def run(self):
        Gui.window.mainloop()