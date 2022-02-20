import pandas as pd

tabela_transformers = "BD_transformers.xlsx"
tabela_drive = "BD_Drive.xlsx"

transformers = pd.read_excel(tabela_transformers)
drive = pd.read_excel(tabela_drive)

#VALOR PROCURADO
search = "300-Louveira"

Resultado = transformers.loc[transformers["Rotas"]== search]

print(Resultado)