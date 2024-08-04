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
A EloGroup ganhou uma licitação pública na Secretária da Fazenda de um determinado estado. O objetivo é analisar as receitas acumuladas do último semestre, a fim de planejar o orçamento para próximo período.

Tarefa:
O que esperamos nesse momento é que você, como estagiário de engenharia de dados da EloGroup, demonstre conhecimento dos dados disponibilizados e consiga desenvolver um script em SQL para responder a questão abaixo.

Pergunta:
Desenvolva um script SQL para calcular a receita acumulada para os meses disponíveis em 2023, de acordo com a tabela de receita ao lado.

"""


"""
-- Criação da tabela
CREATE TABLE revenue (
    id_revenue INT PRIMARY KEY,
    actual_revenue DECIMAL(15, 2),
    period VARCHAR(7)
);

-- Inserção dos dados
INSERT INTO revenue (id_revenue, actual_revenue, period) VALUES
(1, 8748441.22, '2023-01'),
(2, 10487444.59, '2023-02'),
(3, 7481457.15, '2023-03'),
(4, 7497441.89, '2023-04'),
(5, 8697415.36, '2023-05'),
(6, 12497441.56, '2023-06');

-- Consulta para calcular a receita acumulada
SELECT 
    period,
    actual_revenue,
    SUM(actual_revenue) OVER (ORDER BY period) AS accumulated_revenue
FROM 
    revenue
ORDER BY 
    period;
    
"""