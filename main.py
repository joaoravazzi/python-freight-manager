import tkinter as tk # biblioteca de interface gráfica para python

from tkinter import ttk # o ttk são os widgets do python (coisas que posso interagir)

from funcoes import *

#vamos criar a nossa tela
root = tk.Tk() #cria a tela principal do sistema

root.title('Projeto Scrum - Logística')
root.geometry('400x300') #cria o tamanho da tela ('largura x altura')

# --- CABEÇALHO ---
cabecalho = ttk.Label(
    root, # qual tela ele vai
    text = 'Logística Alpha', # qual a informação
    font = ('Arial', 20, 'bold') #qual a fonte
)
cabecalho.pack(pady=20) # atribuir na tela
# --- FIM CABEÇALHO ---

# --- INFORMAÇÃO ---
informacao = ttk.Label(
    root,
    text = 'Frete mais rápido é aqui',
    font = ('Arial', 10, 'italic')
)
informacao.pack(pady=5)
# --- FIM INFORMAÇÃO

# --- CRIAR A ÁREA DOS BOTÕES ---
tela_btn = ttk.Frame(root) # criei um espaço para os botoes e coloquei na tela principal (root)
tela_btn.pack(pady=20)

# --- CRIAR OS BOTÕES ---
btn_ver_frete = ttk.Button(tela_btn, text='Ver Fretes', width=17, command=exibir_fretes) # ttk.Button(ONTE, TEXTO)
btn_add_frete = ttk.Button(tela_btn, text='Adicionar Fretes', width=17, command=abrir_formulario_frete)
btn_ver_cliente = ttk.Button(tela_btn, text='Ver Clientes', width=17, command=exibir_clientes)
btn_add_cliente = ttk.Button(tela_btn, text='Adicionar Clientes', width=17, command=abrir_formulario_cliente)

# exibir os btns
# para ver os btns eu crio uma tabela e falo qual linha e qual coluna vai exibir
btn_ver_frete.grid(row=0, column=0, pady=10, padx=10) 
btn_add_frete.grid(row=1, column=0, pady=10, padx=10)
btn_ver_cliente.grid(row=0, column=1, pady=10, padx=10)
btn_add_cliente.grid(row=1, column=1, pady=10, padx=10)


root.mainloop() # para ver a tela