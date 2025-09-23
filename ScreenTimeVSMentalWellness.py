### Screen Time vs Mental Wellness Survey

import pandas as pd 
import os

caminho = 'c:/Users/karen.quiroga/Desktop/Python/Clarify_Python/Karen_quiroga/Case_1/'
arquivo = 'ScreenTimevsMentalWellness.csv'
caminhoCompleto = os.path.join(caminho,arquivo)

# ler arquivo 
df = pd.read_csv(caminhoCompleto)
##print(df.head(100))

##print (df.columns.tolist())

 # ----------------------------------------------- LIMBEZA DE DADOS -------------------------------------------------------------
"Verificando se extiste linhas com dados nulos por coluna"
print(df.isnull().sum())


"Removendo linhas somente com valores nulos em linhas espefícicas, caso necessário"

df_semNulos = df.dropna(subset=['age', 'gender', 'user_id', 'screen_time_hours'])

linhasAntes = df.shape[0]
linhasDepois = df_semNulos.shape[0]

print (f' Total de {linhasAntes} linhas antes')
print (f' Total de {linhasDepois} linhas depois')

if linhasAntes > linhasDepois: 
    print(f'Total de {linhasAntes -linhasDepois} linhas excluídas')
else:
    print ('Nenhuma linha excluída')


" Verificnado se existem dados duplicados"

print(df.duplicated()) # exibindo os itens duplicados, caso exista.
print (f'numero de linhas duplicadas: {df.duplicated().sum()}')

# ----------------------------------------------- METRICAS GERAIS ----------------------------------------------------------------------

