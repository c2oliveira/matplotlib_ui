import pandas as pd
import tkinter as tk
from tkinter import ttk

# Criando o DataFrame com os dados fornecidos
data = {
    "Data": ["15/01/2025"] * 5,
    "Cidade": ["São Paulo", "Rio de Janeiro", "Curitiba", "Porto Alegre", "Salvador"],
    "Temperatura Máxima (°C)": [30.5, 35.0, 24.0, 28.0, 31.0],
    "Temperatura Mínima (°C)": [22.0, 25.0, 18.0, 20.0, 24.5],
    "Precipitação (mm)": [12.0, None, 8.0, 15.0, None],
    "Umidade Relativa (%)": [78, 70, None, 82, 80],
}

df = pd.DataFrame(data)

# Substituir valores ausentes

df["Precipitação (mm)"].fillna(df["Precipitação (mm)"].mean(), inplace=True)
df["Umidade Relativa (%)"].fillna(df["Umidade Relativa (%)"].median(), inplace=True)
df["Amplitude Térmica"] = df["Temperatura Máxima (°C)"] - df["Temperatura Mínima (°C)"]

df = df[["Data", "Cidade", "Temperatura Máxima (°C)", "Temperatura Mínima (°C)", 
         "Amplitude Térmica", "Precipitação (mm)", "Umidade Relativa (%)"]]

def create_ui():
    root = tk.Tk()
    root.title("Previsão do Tempo")
    root.geometry("800x300")
    
    frame = ttk.Frame(root, padding=10)
    frame.pack(fill=tk.BOTH, expand=True)
    
    tree = ttk.Treeview(frame, columns=list(df.columns), show='headings')
    
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER)
    
    for index, row in df.iterrows():
        tree.insert("", tk.END, values=list(row))
    
    tree.pack(fill=tk.BOTH, expand=True)
    root.mainloop()

create_ui()
