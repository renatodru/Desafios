###cabeçalho do teste
"""
Teste Técnico DE - Python e SQL
Esta é a primeira etapa do desafio técnico para o processo seletivo da vaga de estágio em Engenharia de Dados da EloGroup. Nosso principal objetivo com esta etapa é avaliar seu nível de conhecimento nas linguagens de programação Python e SQL. Caso você seja aprovado, na próxima etapa você precisará apresentar os códigos e como você chegou aos resultados em uma case interview. O questionário é composto por 6 perguntas, e todo o questionário deve ser respondido em até 180 minutos. Uma vez que tenha iniciado o teste, você deve respondê-lo até o final, e caso o tempo acabe, as respostas serão automaticamente enviadas. Você terá até o dia 04/08 para realizar o teste.

Esta é a primeira etapa do desafio técnico para o processo seletivo da vaga de estágio em Engenharia de Dados da EloGroup. Nosso principal objetivo com esta etapa é avaliar seu nível de conhecimento nas linguagens de programação Python e SQL.

Caso você seja aprovado, na próxima etapa você precisará apresentar os códigos e como você chegou aos resultados em uma case interview.



O questionário é composto por 6 perguntas, e todo o questionário deve ser respondido em até 180 minutos. Uma vez que tenha iniciado o teste, você deve respondê-lo até o final, e caso o tempo acabe, as respostas serão automaticamente enviadas.


Certifique-se de reservar tempo suficiente para fazer o teste.
Caso você saia do teste sem finalizá-lo, o teste será considerado como concluído e você não poderá fazer novamente.
"""

"""
A pergunta possui uma imagem em que é mostrado um print de uma tabela, coluna data no formato yyyy-mm-dd, account_id, user_id

Contexto:
Com o atual crescimento da companhia, nos deparamos com a necessidade de auditar as licenças de softwares da empresa, com o objetivo de entender quais colaboradores realmente têm acesso ao sistema e o utiliza de forma recorrente, a fim de ceder licenças apenas para quem de fato o utiliza.

Tarefa:
O que esperamos nesse momento é que você, como estagiário de engenharia de dados da EloGroup, demonstre conhecimento dos dados disponibilizados e consiga desenvolver um código python para responder à pergunta abaixo.

Pergunta:
Desenvolva um código em python para encontrar todos os usuários que estão ativos por três dias consecutivos, baseado nos dados que estão na imagem ao lado.
Marque o user_id que ficou ativo por três dias consecutivos, de acordo com o resultado do seu código:
"""

import pandas as pd
from io import StringIO

# Creating a DataFrame from the manually extracted data
data = """
Date,account_id,User_id
2020-12-06,A1,U1
2021-01-15,A1,U2
2021-01-06,A1,U3
2021-01-02,A1,U1
2020-12-24,A1,U2
2020-12-08,A1,U1
2020-12-09,A1,U1
2021-01-10,A1,U4
2021-01-11,A1,U4
2021-01-12,A2,U4
2020-12-17,A2,U5
2020-12-25,A2,U4
2021-01-01,A2,U6
2020-12-15,A2,U5
2020-12-17,A3,U7
2020-12-06,A3,U6
2021-01-08,A3,U6
2021-02-07,A1,U1
2021-02-10,A1,U1
2021-02-01,A2,U4
2021-02-01,A4,U4
2021-02-01,A2,U5
"""

df = pd.read_csv(StringIO(data), parse_dates=['Date'])

# Sorting the DataFrame by User_id and Date
df = df.sort_values(by=['User_id', 'Date'])

# Inicializando uma lista para armazenar os user_ids ativos por três dias consecutivos
usuarios_ativos_consecutivos = []

# Percorrendo os dados agrupados por 'User_id'
for user_id, grupo in df.groupby('User_id'):
    # Reiniciando o índice do grupo
    grupo = grupo.reset_index(drop=True)
    
    # Verificando se há três dias consecutivos de atividade
    for i in range(len(grupo) - 2):
        if (grupo.loc[i + 1, 'Date'] - grupo.loc[i, 'Date']).days == 1 and (grupo.loc[i + 2, 'Date'] - grupo.loc[i + 1, 'Date']).days == 1:
            usuarios_ativos_consecutivos.append(user_id)
            break

# Exibindo os user_ids que ficaram ativos por três dias consecutivos
print("Usuários ativos por três dias consecutivos:", usuarios_ativos_consecutivos)