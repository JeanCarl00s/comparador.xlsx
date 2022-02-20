from tkinter import N
from matplotlib import transforms
import pandas as pd

tabela_transformers = "BD_transformers.xlsx"
tabela_drive = "BD_Drive.xlsx"

transformers = pd.read_excel(tabela_transformers)
drive = pd.read_excel(tabela_drive)

print("Tabela Drive\n", drive)
print("Tabela Transformers\n", transformers)