###cabeçalho do teste
"""
Teste Técnico DE - Python e SQL
Esta é a primeira etapa do desafio técnico para o processo seletivo da vaga de estágio em Engenharia de Dados da EloGroup. Nosso principal objetivo com esta etapa é avaliar seu nível de conhecimento nas linguagens de programação Python e SQL. Caso você seja aprovado, na próxima etapa você precisará apresentar os códigos e como você chegou aos resultados em uma case interview. O questionário é composto por 6 perguntas, e todo o questionário deve ser respondido em até 180 minutos. Uma vez que tenha iniciado o teste, você deve respondê-lo até o final, e caso o tempo acabe, as respostas serão automaticamente enviadas. Você terá até o dia 04/08 para realizar o teste.

Esta é a primeira etapa do desafio técnico para o processo seletivo da vaga de estágio em Engenharia de Dados da EloGroup. Nosso principal objetivo com esta etapa é avaliar seu nível de conhecimento nas linguagens de programação Python e SQL.

Caso você seja aprovado, na próxima etapa você precisará apresentar os códigos e como você chegou aos resultados em uma case interview.



O questionário é composto por 6 perguntas, e todo o questionário deve ser respondido em até 180 minutos. Uma vez que tenha iniciado o teste, você deve respondê-lo até o final, e caso o tempo acabe, as respostas serão automaticamente enviadas.


Certifique-se de reservar tempo suficiente para fazer o teste.
Caso você saia do teste sem finalizá-lo, o teste será considerado como concluído e você não poderá fazer novamente.


Contexto:
A EloGroup foi acionada por uma grande empresa de minério com o propósito de realizar um projeto de People Analytics, que visa analisar as pessoas, os cargos, salários e quantidade de mulheres em cargos de lideranças para, assim, garantir equidade dos salários.

Tarefa:
O que esperamos nesse momento é que você, como estagiário de engenharia de dados da Elogroup, demonstre conhecimento dos dados disponibilizados e consiga desenvolver um código python para responder a pergunta abaixo.

Pergunta:
Desenvolva um código em python para buscar o cargo que tem os salários mais altos na companhia, baseando-se nas duas tabelas que estão abaixo.
Marque os cargos que têm os salários mais altos da companhia, de acordo com resultado do seu código:

"""


import pandas as pd

data_1 = {
    "Worker_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "name": ["Lucas", "Arthur", "Alfred", "Thiago", "Thais", "Angela", "Ramon", "Bernado", "Ligia", "Rafael", "Nadine", "Luan"],
    "last_name": ["Mendes", "Vern", "Singal", "Kumar", "argônio", "patel", "Silva", "Costa", "Lamas", "Meira", "Schmit", "Lien"],
    "salary": [100000, 80000, 300000, 500000, 500000, 200000, 75000, 90000, 90000, 65000, 75000, 85000],
    "joining_date": ["20/02/2014", "11/06/2014", "20/02/2014", "20/02/2014", "11/06/2014", "11/06/2014", "20/01/2014", "11/04/2014", "10/04/2015", "11/04/2015", "20/03/2014", "21/03/2014"],
    "department": ["RH", "Administrador", "RH", "Administrador", "Administrador", "Contas a pagar", "Contas a pagar", "TI", "Administrador", "TI", "Contas a pagar", "RH"]
}

data_2 = {
    "Worker_ref_id": [1, 2, 8, 5, 4, 7, 6],
    "worker_title": ["Gerente", "Executivo", "Executivo", "Gerente", "Gerente Associado", "Gerente de projetos", "Lider"],
    "affected_from": ["20/02/2016", "11/06/2016", "11/06/2016", "11/06/2016", "11/06/2016", "11/06/2016", "11/06/2016"]
}

# Convertendo os dicionários em DataFrames
df1 = pd.DataFrame(data_1)
df2 = pd.DataFrame(data_2)

# Fazendo o merge das duas tabelas
df_merged = pd.merge(df1, df2, left_on='Worker_id', right_on='Worker_ref_id', how='left')
#print(df_merged)

# Encontrando o salário máximo
salario_maximo = df_merged['salary'].max()

# Identificando os cargos com o salário máximo
cargos_com_salario_maximo = df_merged[df_merged['salary'] == salario_maximo]['worker_title'].unique()

# Exibindo os cargos com os salários mais altos
print("Cargos com os salários mais altos da companhia:", cargos_com_salario_maximo)




