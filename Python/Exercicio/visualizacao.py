import csv
import os
from sys import argv

import pandas as pd
import seaborn as sns

# extraindo as colunas hora e taxa
arquivo = os.path.join(r'taxa-cdi.csv')
df = pd.read_csv(arquivo)

# salvando no grafico
grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
_ = grafico.set_xticks(range(0, len(df['hora'])))
_ = grafico.set_xticklabels(labels=df['hora'], rotation=90)
grafico.get_figure().savefig("graf-cdi.png")
