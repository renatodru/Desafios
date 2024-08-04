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
A EloGroup está desenvolvendo um projeto de Analytics em uma empresa gás em São Paulo, e o objetivo inicial é classificar os funcionários com base nos seus salários por departamento, para pensarem em uma adequação de plano de cargos de salários para companhia.

Tarefa:
O que esperamos nesse momento é que você, como estagiário de engenharia de dados da Elogroup, demonstre conhecimento dos dados disponibilizados e consiga desenvolver um script em SQL para responder a questão abaixo.

Pergunta:
Desenvolva um script em SQL para classificar os funcionários com base nos seus salários, mas agrupados por departamento. Além disso, queremos exibir o número total de funcionários em cada departamento e o salário médio dentro de cada departamento. Para isso, utilize como base a tabela de funcionários ao lado.


"""

"""
SELECT 
    departament, 
    name, 
    last_name, 
    salary,
    RANK() OVER (PARTITION BY departament ORDER BY salary DESC) AS ranking,
    COUNT(*) OVER (PARTITION BY departament) AS total_funcionarios,
    AVG(salary) OVER (PARTITION BY departament) AS salario_medio 
FROM 
    employee;
"""