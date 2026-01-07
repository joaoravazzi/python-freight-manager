# 🚚 Logística Alpha 

Sistema desktop desenvolvido em **Python** para facilitar o controle de operações logísticas, permitindo o cadastro organizado de fretes e clientes com interface gráfica intuitiva.

## 🎯 Sobre o Projeto

Este projeto foi feito durante o Bootcamp da Generation Brasil e estruturado com foco em modularização e persistência de dados local. Ele resolve o problema de registros manuais ao oferecer formulários específicos que validam e salvam as informações diretamente em arquivos estruturados.

---

## 📸 Demonstração do Sistema

### 🖥️ Tela Principal
A porta de entrada do sistema, onde o usuário escolhe entre gerenciar fretes ou clientes.

<p align="center">
  <img src="https://github.com/user-attachments/assets/cc95d940-67f2-44c2-9005-4346006243a4" alt="Tela Principal" width="400">
</p>

---

### 📦 Gestão de Fretes
Módulo para cadastrar novas rotas e visualizar o status dos transportes em tempo real.

| Cadastro de Frete | Visualização de Fretes |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/b6fa16f5-85a8-4f02-a052-af2fe9238923" width="300"> | <img src="https://github.com/user-attachments/assets/84032c7f-8ffd-499b-8983-cdcebd266d9f" width="500"> |

---

### 👥 Gestão de Clientes
Controle completo da base de clientes atendidos pela Logística Alpha.

| Cadastro de Clientes | Visualização de Clientes |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/5ce10384-e50d-45f1-ac8f-d4a1e3236c0a" width="300"> | <img src="https://github.com/user-attachments/assets/4bbf4aba-8237-480a-aacc-2ca91174a6dc" width="500"> |
## ✨ Funcionalidades
* **Gestão de Fretes:** Interface para cadastro de registros com campos de Origem, Destino, Cliente, Produto e Status.
* **Gestão de Clientes:** Formulário dedicado para registro de novos clientes com Nome, Sobrenome, Cidade e Bairro.
* **Visualização em Tempo Real:** Tabela dinâmica (Treeview) para exibir todos os fretes salvos no sistema.
* **Armazenamento em CSV:** Utiliza o formato CSV para garantir que os dados não sejam perdidos ao fechar o programa.
* **Interface Amigável:** Menu principal organizado com botões de acesso rápido para as principais funções.

## 🛠️ Tecnologias
* **Python 3**
* **Tkinter/TTK:** Para a construção da interface gráfica.
* **CSV & OS:** Para manipulação de arquivos e caminhos do sistema operacional.

## 📂 Estrutura de Arquivos
* `main.py`: Arquivo principal que inicia a aplicação e contém o menu.
* `funcoes.py`: Contém toda a lógica de criação de janelas (popups), leitura e escrita de arquivos.
* `dados_fretes.csv`: Base de dados para registros de transporte.
* `dados_clientes.csv`: Base de dados para registros de clientes.

---

## ▶️ Como Executar o Projeto

### Pré-requisitos

- Python 3 instalado

### Passo a passo

**1.** Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```
**2.** Acesse a pasta do projeto:
```bash
cd projeto-logistica
```
**3.** Execute o sistema:
```bash
python main.py
```
O sistema abrirá uma interface gráfica onde será possível cadastrar e visualizar fretes e clientes.

## 🎯 Objetivo do Projeto

* Praticar Python na prática

* Criar interfaces gráficas com Tkinter

* Trabalhar com manipulação de arquivos CSV

* Organizar código separando responsabilidades

* Simular um sistema real de logística

## 🚀 Possíveis Melhorias Futuras

* Validação de campos obrigatórios

* Adicionar botão para excluir ou editar registros existentes.

* Integração com banco de dados (SQLite ou MySQL)

* Melhorias no layout da interface

---

*📌 Projeto desenvolvido para fins de aprendizado e prática.*
