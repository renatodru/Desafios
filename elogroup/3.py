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
A EloGroup lançou um aplicativo interno para cadastro e acompanhamento de projetos, visando ter maior assertividade na governança e gestão dos projetos.

Tarefa:
O que esperamos nesse momento é que você, como estagiário de engenharia de dados da Elogroup, demonstre conhecimento dos dados disponibilizados e consiga desenvolver um código python para responder à questão abaixo.

Pergunta:
Desenvolva um código em python para comparar as taxas de retenção em janeiro de 2023 com as de dezembro de 2022. A taxa de retenção é definida como a porcentagem de colaboradores que uma empresa retém durante um determinado período de tempo, baseando-se na tabela ao lado.
Quais account_id tiveram a maior taxa de retenção?

"""


import pandas as pd

dados = {
    "Date": ["01/01/2023", "01/01/2023", "06/01/2023", "02/01/2023", "24/12/2022", 
             "08/12/2022", "09/12/2022", "10/01/2023", "11/01/2023", "12/01/2023", 
             "15/01/2023", "17/12/2022", "25/12/2022", "25/12/2022", "25/12/2022", 
             "06/12/2022", "06/12/2022", "14/01/2023", "07/02/2023", "10/02/2023", 
             "01/02/2023", "01/02/2023", "05/12/2022"],
    "account_id": ["A1", "A1", "A1", "A1", "A1", "A1", "A1", "A2", "A2", "A2", "A2", "A2", "A3", "A3", "A3", "A3", 
                   "A3", "A4", "A1", "A1", "A4", "A2", "A1"],
    "user_id": ["USER1", "USER2", "USER3", "USER1", "USER2", "USER1", "USER1", "USER4", "USER4", "USER4", "USER5", 
                "USER4", "USER6", "USER6", "USER6", "USER7", "USER6", "USER6", "USER1", "USER2", "USER4", "USER5", "USER8"]
}

# Convertendo os dados para um DataFrame
# Convertendo o dicionário em um DataFrame
df = pd.DataFrame(dados)

# Convertendo a coluna 'Date' para o formato de data
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Filtrando os dados para dezembro de 2022 e janeiro de 2023
df_202212 = df[(df['Date'] >= '2022-12-01') & (df['Date'] < '2023-01-01')].sort_values('account_id')
df_202301 = df[(df['Date'] >= '2023-01-01') & (df['Date'] < '2023-02-01')].sort_values('account_id')
print(df_202212)
print('\n')
print(df_202301)

# Calculando a retenção por account_id
retenção = {}
print(df['account_id'].unique())
for account in df['account_id'].unique():
    users_202212 = set(df_202212[df_202212['account_id'] == account]['user_id'])
    users_202301 = set(df_202301[df_202301['account_id'] == account]['user_id'])
    print(users_202212)
    print(users_202301)
    print('\n')
    if users_202212:
        retenção[account] = len(users_202301 & users_202212) / len(users_202212) * 100
    else:
        retenção[account] = 0

# Identificando os account_id com a maior taxa de retenção
maior_retenção = max(retenção.values())
accounts_maior_retenção = [account for account, taxa in retenção.items() if taxa == maior_retenção]

# Exibindo os account_id com a maior taxa de retenção
print("Account_id com a maior taxa de retenção:", accounts_maior_retenção)
print("Taxas de retenção:", retenção)


