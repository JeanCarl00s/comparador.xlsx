from asyncio.windows_events import NULL
from sys import api_version
from numpy import empty
import pandas as pd



tabela_transformers = "BD_transformers.xlsx"
tabela_drive = "BD_Drive.xlsx"

transformers = pd.read_excel(tabela_transformers)
drive = pd.read_excel(tabela_drive)
    
indice = 0
RotaDrive = drive.loc[indice, "Rotas"]
Resultado = transformers.loc[transformers["Rotas"]== RotaDrive]
    

for x in Resultado:  
    print(Resultado)
    indice = indice + 1
    #PROCURA A ROTA QUE TEM AQUELE INDICE
    RotaDrive = drive.loc[indice, "Rotas"]
    Resultado = transformers.loc[transformers["Rotas"]== RotaDrive]
    if Resultado.empty:
        print("----- Rota nao encontrada-----\n")
        RotaError = drive.loc[drive["Rotas"]== RotaDrive]
        print("numero do indice", indice ," da Rota \n", RotaError)
    

#LOCALIZAR NA TABELA DO TRANSFORMERS O NOME DA ROTA IGUAL AO ROTADRIVE E SUA DESCRICAO 
#Resultado = transformers.loc[transformers["Rotas"]== RotaDrive, "Descricao"] 


