import csv
import os # sao funçoes do sistema operacional(operational system)
import tkinter as tk
from tkinter import ttk

dados_fretes = 'dados_fretes.csv'

campo_fretes = ['Registro_frete','Origem','Destino','Cliente','Produto','Status']

# Funções

# adicionar_registo_frete - segurança pro sistema
# abrir_formulario_frete - criar uma tela pra add as infos
# salvar_o_frete - atualizar o csv

def abrir_formulario_frete():
    popup_frete = tk.Toplevel()
    popup_frete.title('Adicionar Fretes')
    popup_frete.geometry('400x400')
    
    labels_fretes = ['Registro_frete','Origem','Destino','Cliente','Produto','Status']
    fretes = {}
    
    # sequenciar campo com dados
    for campo_dados in labels_fretes: # para cada campo que o usuario digita, ele faz algo
        tk.Label(popup_frete, text=campo_dados + ':').pack(pady=5) # essa linha cria todos os textos para o usuario
        entrada_fretes = tk.Entry(popup_frete) # entry é análogo ao input (caixa de texto)
        entrada_fretes.pack()
        fretes[campo_dados] = entrada_fretes
       
    def salvar():
        dados = {campo_dados:fretes[campo_dados].get() for campo_dados in fretes}
        add_fretes(dados)
        popup_frete.destroy() # fechar automatico uma janela 
     
    tk.Button(popup_frete, text='SALVAR', pady=5, command=salvar).pack(side='left', padx=20, pady=20, expand=True)
    tk.Button(popup_frete, text='LIMPAR', pady=5).pack(side='left', padx=20, pady=20, expand=True)
    
def add_fretes(registro):
    arquivo = os.path.isfile(dados_fretes) # para manipular o arquivo
    
    # add valores
    with open(dados_fretes, 'a', newline='', encoding='utf-8') as arquivo_fretes: # sempre que usamos o with open, informamos 1 - arquivo, 2 - modo, 3- novas linhas, 4 - utf-8
        escrever = csv.DictWriter(arquivo_fretes, fieldnames=campo_fretes)
        escrever.writerow(registro) # para adicionar os dados do csv
        

dados_clientes = 'dados_clientes.csv'

campo_clientes = ['Registro_cliente','Nome','Sobrenome','Cidade','Bairro']

# Funções

def abrir_formulario_cliente():
    popup_cliente = tk.Toplevel()
    popup_cliente.title('Adicionar Clientes')
    popup_cliente.geometry('400x400')
    
    labels_clientes = ['Registro_cliente','Nome','Sobrenome','Cidade','Bairro']
    clientes = {}
    
    # sequenciar campo com dados
    for campo_dados_c in labels_clientes: # para cada campo que o usuario digita, ele faz algo
        tk.Label(popup_cliente, text=campo_dados_c + ':').pack(pady=5) # essa linha cria todos os textos para o usuario
        entrada_clientes = tk.Entry(popup_cliente) # entry é análogo ao input (caixa de texto)
        entrada_clientes.pack()
        clientes[campo_dados_c] = entrada_clientes
       
    def salvar_c():
        dados_c = {campo_dados_c:clientes[campo_dados_c].get() for campo_dados_c in clientes}
        add_clientes(dados_c)
        popup_cliente.destroy() # fechar automatico uma janela 
     
    tk.Button(popup_cliente, text='SALVAR', pady=5, command=salvar_c).pack(side='left', padx=20, pady=20, expand=True)
    tk.Button(popup_cliente, text='LIMPAR', pady=5).pack(side='left', padx=20, pady=20, expand=True)
    
def add_clientes(registro_c):
    arquivo_c = os.path.isfile(dados_clientes) # para manipular o arquivo
    
    # add valores
    with open(dados_clientes, 'a', newline='', encoding='utf-8') as arquivo_clientes: # sempre que usamos o with open, informamos 1 - arquivo, 2 - modo, 3- novas linhas, 4 - utf-8
        escrever = csv.DictWriter(arquivo_clientes, fieldnames=campo_clientes)
        escrever.writerow(registro_c) # para adicionar os dados do csv
        
def exibir_fretes():
    if not os.path.isfile(dados_fretes): # sempre que for exibir dados, colocar fator correção
        tk.Message.showerror('ERRO',"ARQUIVO NÃO ENCONTRADO")
        return
    
    #criar a janela da tabela de fretes
    janela_fretes = tk.Toplevel()
    janela_fretes.title('Fretes')
    janela_fretes.geometry('750x500')
    
    #quero dizer para a tabela os capos que ela tem (as colunas)
    colunas_fretes = campo_fretes
    
    # vamos juntar a tabela com as colunas (modo arvore)
    tabela_fretes = ttk.Treeview(janela_fretes, columns=colunas_fretes, show='headings') # o treeview é o comando para mostrar os dados, nele tenho que coloca 1) onde, 2) colunas, 3) meus cabeçalhos
    tabela_fretes.pack(fill='both')
    
    # configuração de colunas
    for colunas in colunas_fretes:
        tabela_fretes.heading(colunas, text=colunas) # chamo o campo cabeçalho para escrever o cabeçalho das colunas
        tabela_fretes.column(colunas, width=120) # chamo o campo column para configurar o tamanho de cada uma
    
    with open(dados_fretes, 'r', encoding='utf-8') as arquivo:  # ler os dados do csv
        leitor = csv.DictReader(arquivo)
        
        for linha in leitor:  # mostrar o csv
            valor = [linha.get(colunas,'') for colunas in colunas_fretes]  # para cada linha do csv que o leitor leu, eu vou criar um campo com valor
            tabela_fretes.insert('','end',values=valor)  # o comando insert é para colocar os valores nas linhas e nas colunas
            
def exibir_clientes():
    if not os.path.isfile(dados_fretes):
        tk.Message.showerror('ERRO',"ARQUIVO NÃO ENCONTRADO")
        return
        
    janela_clientes = tk.Toplevel()
    janela_clientes.title('Fretes')
    janela_clientes.geometry('750x500')
    
    colunas_clientes = campo_clientes
    
    tabela_clientes = ttk.Treeview(janela_clientes, columns=colunas_clientes, show='headings')
    tabela_clientes.pack(fill='both')
        
    for colunas in colunas_clientes:
        tabela_clientes.heading(colunas, text=colunas)
        tabela_clientes.column(colunas, width=120)
    
    with open(dados_fretes, 'r', encoding='utf-8') as arquivo_c:
        leitor = csv.DictReader(arquivo_c)
        
        for linha in leitor:
            valor_c = [linha.get(colunas,'') for colunas in colunas_clientes]
            tabela_clientes.insert('','end',values=valor_c)