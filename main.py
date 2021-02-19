import pandas as pd

dados = pd.read_csv('C:\\Users\\Thiago\\Desktop\\Transferencias.csv',
                        encoding='cp1252', sep=';',
                        engine='python', header=0)

dadosPB = dados[(dados.UF == "PB")]

print(dadosPB)

dadosPB.to_excel(r'C:\\Users\\Thiago\\Desktop\\Transferencias.xlsx', index=False)
