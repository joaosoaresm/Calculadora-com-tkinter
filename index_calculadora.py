from index_propriedades import *
import tkinter as tk
from tkinter import messagebox

def realizar_operacao():
    try:
        x = int(entry_x.get())
        y = int(entry_y.get())
        operacao = var_operacao.get()

        if operacao == 1:
            result = soma(x, y)
            operacao_str = "soma"
            simbolo = "+"
        elif operacao == 2:
            result = subtracao(x, y)
            operacao_str = "subtração"
            simbolo = "-"
        elif operacao == 3:
            result = multiplicacao(x, y)
            operacao_str = "multiplicação"
            simbolo = "x"
        elif operacao == 4:
            result = divisao(x, y)
            operacao_str = "divisão"
            simbolo = "/"
        
        messagebox.showinfo("Resultado", f'Resultado da {operacao_str} de {x} {simbolo} {y} = {result}')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def nova_operacao():
    entry_x.delete(0, tk.END)
    entry_y.delete(0, tk.END)
    var_operacao.set(1)

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora")

# Variável para armazenar a operação selecionada
var_operacao = tk.IntVar(value=1)

# Frame para organizar a interface
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Widgets para selecionar a operação
tk.Label(frame, text="Selecione a operação:", font=('Arial', 14)).grid(row=0, column=0, columnspan=2, pady=5)
tk.Radiobutton(frame, text="Soma", variable=var_operacao, value=1, font=('Arial', 12)).grid(row=1, column=0, sticky='w')
tk.Radiobutton(frame, text="Subtração", variable=var_operacao, value=2, font=('Arial', 12)).grid(row=1, column=1, sticky='w')
tk.Radiobutton(frame, text="Multiplicação", variable=var_operacao, value=3, font=('Arial', 12)).grid(row=2, column=0, sticky='w')
tk.Radiobutton(frame, text="Divisão", variable=var_operacao, value=4, font=('Arial', 12)).grid(row=2, column=1, sticky='w')

# Widgets para entrada dos valores
tk.Label(frame, text="Digite um valor para X:", font=('Arial', 14)).grid(row=3, column=0, pady=5, sticky='e')
entry_x = tk.Entry(frame, font=('Arial', 14))
entry_x.grid(row=3, column=1, pady=5)

tk.Label(frame, text="Digite um valor para Y:", font=('Arial', 14)).grid(row=4, column=0, pady=5, sticky='e')
entry_y = tk.Entry(frame, font=('Arial', 14))
entry_y.grid(row=4, column=1, pady=5)

# Botão para realizar a operação
tk.Button(frame, text="Calcular", command=realizar_operacao, font=('Arial', 14)).grid(row=5, column=0, columnspan=2, pady=10)

# Botão para nova operação
tk.Button(frame, text="Nova Operação", command=nova_operacao, font=('Arial', 14)).grid(row=6, column=0, columnspan=2, pady=5)

# Iniciar o loop da aplicação
root.mainloop()