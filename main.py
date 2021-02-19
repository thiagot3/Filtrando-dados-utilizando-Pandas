#importando o pandas.
import pandas as pd

# Lendo arquivo .CVS e salvando em um Pandas DataFrame
dados = pd.read_csv('C:\\...\\arquivo.csv',
                        encoding='cp1252', sep=';',
                        engine='python', header=0)

# Filtrando dados na variável dadosPB
dadosPB = dados[(dados.UF == "PB")]

# Exportando para um arquivo Exel
dadosPB.to_excel(r'C:\\...\\arquivo.xlsx', index=False)
