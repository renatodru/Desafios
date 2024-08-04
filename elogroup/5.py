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
A EloGroup está realizando internamente uma auditoria para verificar os consultores que mais conseguiram angariar novos projetos, e entender como potencializar ainda mais essas vendas.

Tarefa:
O que esperamos nesse momento é que você, como estagiário de engenharia de dados da EloGroup, demonstre conhecimento dos dados disponibilizados e consiga desenvolver um script em SQL para responder a questão abaixo.

Pergunta:
Desenvolva um script em SQL para encontrar o consultor que realizou vendas com os valores máximos durante os anos 2021, 2022, 2023, baseando-se na tabela ao lado.

"""

"""
WITH CTE AS (
    SELECT 
        year, 
        consultant_name, 
        sale_amount, 
        branch, 
        ROW_NUMBER() OVER (PARTITION BY year ORDER BY sale_amount DESC) AS row_number 
    FROM yearly_sales
)
SELECT 
    year, 
    consultant_name 
FROM 
    CTE 
WHERE 
    row_number = 1;
    """
