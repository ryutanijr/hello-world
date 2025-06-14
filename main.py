import pandas as pd
import os

# Caminho do arquivo
arquivo_excel = os.path.join("dados", "vendas.xlsx")

# Lê o Excel
df = pd.read_excel(arquivo_excel)

# Processa: resumo por produto
resumo = df.groupby("Produto")["Valor"].sum().reset_index()

# Salva o CSV com o resumo
resumo.to_csv("resumo_vendas.csv", index=False)

print("Resumo de vendas gerado com sucesso.")
