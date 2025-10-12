### Screen Time vs Mental Wellness Survey
###Tratar a base de dados, excluindo valores nulos, ajustando duplicidades conforme necessário 
# e realizando o levantamento de métricas gerais, salvando os dados tratados em csv.

import pandas as pd 
import os

caminho = 'c:/Users/karen.quiroga/Desktop/Python/Clarify_Python/Karen_quiroga/Case_1/'
arquivo = 'ScreenTimevsMentalWellness.csv'
caminhoCompleto = os.path.join(caminho,arquivo)

# ler arquivo 
df = pd.read_csv(caminhoCompleto)

#print(df.head (10))

# print (df.columns.tolist())


 # ----------------------------------------------- LIMBEZA DE DADOS -------------------------------------------------------------
"Verificando se extiste linhas com dados nulos por coluna"
print(df.isnull().sum())

print(df.columns)

# Aqui exclui a ultima coluna que estava em branco
df = df.drop(columns=['Unnamed: 15'])

print(df.isnull().sum())

##print(list(df.columns)) 

" Verificnado se existem dados duplicados"

print(df.duplicated()) # exibindo os itens duplicados, caso exista.
print (f'numero de linhas duplicadas: {df.duplicated().sum()}')


# ----------------------------------------------- METRICAS GERAIS ----------------------------------------------------------------------

# Contar nmúmero de users por age e gender
df_countUser = df.groupby(['age','gender'])['user_id'].nunique()
print (df_countUser)

# Contar múmero total e distintos de users por age e gender
df_countUserAll = df.groupby(['age','gender']). agg({'user_id':['nunique','count']})
print (df_countUserAll)


df_resultado = df.groupby(['occupation','work_mode','gender']). agg({'user_id': 'nunique',
                                                                      'age': 'median',
                                                                      'screen_time_hours': 'median',
                                                                      'work_screen_hours': 'median',
                                                                      'leisure_screen_hours': 'median',
                                                                      'sleep_hours': 'median',
                                                                      'exercise_minutes_per_week':'median',
                                                                      'stress_level_0_10':'median',
                                                                      'productivity_0_100':'median', 
                                                                      'social_hours_per_week': 'median',
                                                                      'mental_wellness_index_0_100': 'median' }).reset_index().round(0)
print (df_resultado)

df_resultado = pd.DataFrame(df_resultado)

df_resultado.to_csv('resultado_consolidado.csv', index = False)
print('Dados salvos em csv')

df.to_csv('raw.csv', index = False)
print('Dados salvos em csv')

"""
Pefuntas as serem respondidas por gráfico
- Média produtividade por tipo de work_mode ( filtrando somente pela occuppation "employed")
- Fazer a comparação acima por genero 
- Entender media_social_hours por week impacta na na produtividade e mental well ness em cada um dos tipos de work mode.
"""
