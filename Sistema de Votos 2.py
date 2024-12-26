import tkinter as tk
from tkinter import ttk, messagebox

# Inicialização das variáveis globais de votos
totalA = 0
totalB = 0
totalC = 0
totalD = 0
totalE = 0
totalF = 0

def contabilizar_votos():
    global totalA, totalB, totalC, totalD, totalE, totalF

    try:
        votosA = int(entry_votosA.get()) if entry_votosA.get() else 0
        votosB = int(entry_votosB.get()) if entry_votosB.get() else 0
        votosC = int(entry_votosC.get()) if entry_votosC.get() else 0
        votosD = int(entry_votosD.get()) if entry_votosD.get() else 0
        votosE = int(entry_votosE.get()) if entry_votosE.get() else 0
        votosF = int(entry_votosF.get()) if entry_votosF.get() else 0
    except ValueError:
        messagebox.showerror("Erro", "Insira um valor numérico válido.")
        return

    totalA += votosA
    totalB += votosB
    totalC += votosC
    totalD += votosD
    totalE += votosE
    totalF += votosF

    totalGeral = totalA + totalB + totalC + totalD + totalE + totalF
    percentualA = (totalA / totalGeral * 100) if totalGeral > 0 else 0
    percentualB = (totalB / totalGeral * 100) if totalGeral > 0 else 0
    percentualC = (totalC / totalGeral * 100) if totalGeral > 0 else 0
    percentualD = (totalD / totalGeral * 100) if totalGeral > 0 else 0
    percentualE = (totalE / totalGeral * 100) if totalGeral > 0 else 0
    percentualF = (totalF / totalGeral * 100) if totalGeral > 0 else 0

    # Atualização dos labels de resultados
    label_totalA.config(text=f"Total de Votos do Candidato A: {totalA}")
    label_totalB.config(text=f"Total de Votos do Candidato B: {totalB}")
    label_totalC.config(text=f"Total de Votos do Candidato C: {totalC}")
    label_totalD.config(text=f"Total de Votos do Candidato D: {totalD}")
    label_totalE.config(text=f"Total de Votos do Candidato E: {totalE}")
    label_totalF.config(text=f"Total de Votos do Candidato F: {totalF}")
    label_totalGeral.config(text=f"Total de Votos Geral: {totalGeral}")

    label_percentualA.config(text=f"Percentual de Votos do Candidato A: {percentualA:.2f}%")
    label_percentualB.config(text=f"Percentual de Votos do Candidato B: {percentualB:.2f}%")
    label_percentualC.config(text=f"Percentual de Votos do Candidato C: {percentualC:.2f}%")
    label_percentualD.config(text=f"Percentual de Votos do Candidato D: {percentualD:.2f}%")
    label_percentualE.config(text=f"Percentual de Votos do Candidato E: {percentualE:.2f}%")
    label_percentualF.config(text=f"Percentual de Votos do Candidato F: {percentualF:.2f}%")

    # Atualização das barras de progresso e labels de porcentagem
    barraA['value'] = percentualA; 
    barraB['value'] = percentualB
    barraC['value'] = percentualC
    barraD['value'] = percentualD
    barraE['value'] = percentualE
    barraF['value'] = percentualF
    barraA_label.config(text=f"{percentualA:.2f}%")
    barraB_label.config(text=f"{percentualB:.2f}%")
    barraC_label.config(text=f"{percentualC:.2f}%")
    barraD_label.config(text=f"{percentualD:.2f}%")
    barraE_label.config(text=f"{percentualE:.2f}%")
    barraF_label.config(text=f"{percentualF:.2f}%")

    # Limpar entradas
    entry_votosA.delete(0, tk.END)
    entry_votosB.delete(0, tk.END)
    entry_votosC.delete(0, tk.END)
    entry_votosD.delete(0, tk.END)
    entry_votosE.delete(0, tk.END)
    entry_votosF.delete(0, tk.END)

# Configuração da janela principal
window = tk.Tk()
window.title("Sistema de Votação")
window.geometry("600x700")
window.configure(bg="#B0FFED")

# Título
title = tk.Label(window, text="Sistema de Votação", font=("Arial", 20, "bold"), bg="#B0FFED", fg="#333")
title.pack(pady=15)

# Criação de Frame com Scrollbar
frame = tk.Frame(window, bg="#B0FFED")
frame.pack(fill="both", expand=True)

# Scrollbar vertical
scrollbar = tk.Scrollbar(frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Área de conteúdo com canvas
canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set, bg="#B0FFED")
canvas.pack(side="left", fill="both", expand=True)

scrollbar.config(command=canvas.yview)

# Contêiner dentro do canvas
frame_content = tk.Frame(canvas, bg="#B0FFED")
canvas.create_window((0, 0), window=frame_content, anchor="nw")

# Widgets dentro do Frame de Conteúdo
# Input Votos A
frame_votosA = tk.Frame(frame_content, bg="#B0FFED")
frame_votosA.pack(pady=8, fill="x")
label_votosA = tk.Label(frame_votosA, text="Votos para o Candidato A:", font=("Arial", 12), bg="#B0FFED")
label_votosA.pack(side=tk.LEFT)
entry_votosA = tk.Entry(frame_votosA, font=("Arial", 12), width=8)
entry_votosA.pack(side=tk.LEFT)

# Input Votos B
frame_votosB = tk.Frame(frame_content, bg="#B0FFED")
frame_votosB.pack(pady=8, fill="x")
label_votosB = tk.Label(frame_votosB, text="Votos para o Candidato B:", font=("Arial", 12), bg="#B0FFED")
label_votosB.pack(side=tk.LEFT)
entry_votosB = tk.Entry(frame_votosB, font=("Arial", 12), width=8)
entry_votosB.pack(side=tk.LEFT)

# Input Votos C
frame_votosC = tk.Frame(frame_content, bg="#B0FFED")
frame_votosC.pack(pady=8, fill="x")
label_votosC = tk.Label(frame_votosC, text="Votos para o Candidato C:", font=("Arial", 12), bg="#B0FFED")
label_votosC.pack(side=tk.LEFT)
entry_votosC = tk.Entry(frame_votosC, font=("Arial", 12), width=8)
entry_votosC.pack(side=tk.LEFT)

# Input Votos D
frame_votosD = tk.Frame(frame_content, bg="#B0FFED")
frame_votosD.pack(pady=8, fill="x")
label_votosD = tk.Label(frame_votosD, text="Votos para o Candidato D:", font=("Arial", 12), bg="#B0FFED")
label_votosD.pack(side=tk.LEFT)
entry_votosD = tk.Entry(frame_votosD, font=("Arial", 12), width=8)
entry_votosD.pack(side=tk.LEFT)

# Input Votos E
frame_votosE = tk.Frame(frame_content, bg="#B0FFED")
frame_votosE.pack(pady=8, fill="x")
label_votosE = tk.Label(frame_votosE, text="Votos para o Candidato E:", font=("Arial", 12), bg="#B0FFED")
label_votosE.pack(side=tk.LEFT)
entry_votosE = tk.Entry(frame_votosE, font=("Arial", 12), width=8)
entry_votosE.pack(side=tk.LEFT)

# Input Votos F
frame_votosF = tk.Frame(frame_content, bg="#B0FFED")
frame_votosF.pack(pady=8, fill="x")
label_votosF = tk.Label(frame_votosF, text="Votos para o Candidato F:", font=("Arial", 12), bg="#B0FFED")
label_votosF.pack(side=tk.LEFT)
entry_votosF = tk.Entry(frame_votosF, font=("Arial", 12), width=8)
entry_votosF.pack(side=tk.LEFT)

# Botão Contabilizar
button = tk.Button(frame_content, text="Contabilizar Votos", font=("Arial", 12, "bold"), bg="#400175", fg="white", command=contabilizar_votos)
button.pack(pady=15, fill="x")

# Resultados
label_resultados = tk.Label(frame_content, text="Resultados:", font=("Arial", 18, "bold"), bg="#B0FFED", fg="#333")
label_resultados.pack()

label_totalA = tk.Label(frame_content, text="Total de Votos do Candidato A: 0", font=("Arial", 12, "bold"), bg="#B0FFED", fg="#00A53e")
label_totalA.pack(fill="x")

label_totalB = tk.Label(frame_content, text="Total de Votos do Candidato B: 0", font=("Arial", 12, "bold"), bg="#B0FFED", fg="#006Abf")
label_totalB.pack(fill="x")

label_totalC = tk.Label(frame_content, text="Total de Votos do Candidato C: 0", font=("Arial", 12, "bold"), bg="#B0FFED", fg="#333")
label_totalC.pack(fill="x")

label_totalD = tk.Label(frame_content, text="Total de Votos do Candidato D: 0", font=("Arial", 12, "bold"), bg="#B0FFED", fg="#FF5733")
label_totalD.pack(fill="x")

label_totalE = tk.Label(frame_content, text="Total de Votos do Candidato E: 0", font=("Arial", 12, "bold"), bg="#B0FFED", fg="#FF69B4")
label_totalE.pack(fill="x")

label_totalF = tk.Label(frame_content, text="Total de Votos do Candidato F: 0", font=("Arial", 12, "bold"), bg="#B0FFED", fg="#9E6C00")
label_totalF.pack(fill="x")

label_totalGeral = tk.Label(frame_content, text="Total de Votos Geral: 0", font=("Arial", 14, "bold"), bg="#B0FFED")
label_totalGeral.pack(fill="x")

# Labels para os percentuais de votos
label_percentualA = tk.Label(frame_content, text="Percentual de Votos do Candidato A: 0.00%", font=("Arial", 12, "bold"), bg="#B0FFED", fg="#00A53e")
label_percentualA.pack(fill="x")

label_percentualB = tk.Label(frame_content, text="Percentual de Votos do Candidato B: 0.00%", font=("Arial", 12, "bold"), bg="#B0FFED", fg="#006Abf")
label_percentualB.pack(fill="x")

label_percentualC = tk.Label(frame_content, text="Percentual de Votos do Candidato C: 0.00%", font=("Arial", 12, "bold"), bg="#B0FFED", fg="#333")
label_percentualC.pack(fill="x")

label_percentualD = tk.Label(frame_content, text="Percentual de Votos do Candidato D: 0.00%", font=("Arial", 12, "bold"), bg="#B0FFED", fg="#FF5733")
label_percentualD.pack(fill="x")

label_percentualE = tk.Label(frame_content, text="Percentual de Votos do Candidato E: 0.00%", font=("Arial", 12, "bold"), bg="#B0FFED", fg="#FF69B4")
label_percentualE.pack(fill="x")

label_percentualF = tk.Label(frame_content, text="Percentual de Votos do Candidato F: 0.00%", font=("Arial", 12, "bold"), bg="#B0FFED", fg="#9E6C00")
label_percentualF.pack(fill="x")


# Barra de progresso
barraA = ttk.Progressbar(frame_content, orient="horizontal", length=200, mode="determinate")
barraA_label = tk.Label(frame_content, text="0.00%", font=("Arial", 10), bg="#B0FFED")
barraA.pack(pady=2, fill="x")
barraA_label.pack(pady=2, fill="x")

barraB = ttk.Progressbar(frame_content, orient="horizontal", length=200, mode="determinate")
barraB_label = tk.Label(frame_content, text="0.00%", font=("Arial", 10), bg="#B0FFED")
barraB.pack(pady=2, fill="x")
barraB_label.pack(pady=2, fill="x")

barraC = ttk.Progressbar(frame_content, orient="horizontal", length=200, mode="determinate")
barraC_label = tk.Label(frame_content, text="0.00%", font=("Arial", 10), bg="#B0FFED")
barraC.pack(pady=2, fill="x")
barraC_label.pack(pady=2, fill="x")

barraD = ttk.Progressbar(frame_content, orient="horizontal", length=200, mode="determinate")
barraD_label = tk.Label(frame_content, text="0.00%", font=("Arial", 10), bg="#B0FFED")
barraD.pack(pady=2, fill="x")
barraD_label.pack(pady=2, fill="x")

barraE = ttk.Progressbar(frame_content, orient="horizontal", length=200, mode="determinate")
barraE_label = tk.Label(frame_content, text="0.00%", font=("Arial", 10), bg="#B0FFED")
barraE.pack(pady=2, fill="x")
barraE_label.pack(pady=2, fill="x")

barraF = ttk.Progressbar(frame_content, orient="horizontal", length=200, mode="determinate")
barraF_label = tk.Label(frame_content, text="0.00%", font=("Arial", 10), bg="#B0FFED")
barraF.pack(pady=2, fill="x")
barraF_label.pack(pady=2, fill="x")

# Função para ajustar o canvas ao conteúdo
def ajustar_canvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", ajustar_canvas)

# Executar a janela principal
window.mainloop()
