import pandas as pd

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

# Substituir valores ausentes na coluna Precipitação pela média da coluna
df["Precipitação (mm)"].fillna(df["Precipitação (mm)"].mean(), inplace=True)

# Substituir valores ausentes na coluna Umidade Relativa pela mediana da coluna
df["Umidade Relativa (%)"].fillna(df["Umidade Relativa (%)"].median(), inplace=True)

# Adicionar a coluna Amplitude Térmica
df["Amplitude Térmica"] = df["Temperatura Máxima (°C)"] - df["Temperatura Mínima (°C)"]

# Criar um novo DataFrame com cidades cuja Temperatura Máxima seja maior que 30°C
df_high_temp = df[df["Temperatura Máxima (°C)"] > 30].copy()

# Reordenar as colunas
column_order = ["Data", "Cidade", "Temperatura Máxima (°C)", "Temperatura Mínima (°C)", 
                "Amplitude Térmica", "Precipitação (mm)", "Umidade Relativa (%)"]

df = df[column_order]
df_high_temp = df_high_temp[column_order]

df, df_high_temp
