import pandas as pd

tabela_transformers = "BD_transformers.xlsx"
tabela_drive = "BD_Drive.xlsx"

transformers = pd.read_excel(tabela_transformers)
drive = pd.read_excel(tabela_drive)

#PEGA TODAS O CIONTEUDO DE CADA COLUNA
for label, content in transformers.items():
    
    print(f'label : {label}')
    print(f'content: {content}', sep='\n')
