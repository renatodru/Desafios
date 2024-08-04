--1.	Crie uma consulta que retorne apenas o item mais pedido e a quantidade total de pedidos.
select 

from tb_products




--2.	Crie uma consulta que retorne todos os clientes que realizaram mais de 4 pedidos no último ano em ordem decrescente.

--3.	Crie uma consulta de quantos pedidos foram realizados em cada mês do último ano.

--4.	Crie uma consulta que retorne APENAS os campos "productName" e "totalAmount" dos 5 produtos mais pedidos.

--5.	Crie uma consulta liste todos os clientes que não realizaram nenhum pedido.

--6.	Crie uma consulta que retorne a data e o nome do produto do último
--pedido realizado pelos clientes onde o customerId são 94, 130, 300 e 1000.

--7.	Com base na estrutura das tabelas fornecidas (tb_order_items, tb_orders, tb_products, tb_customers),
--crie uma nova tabela para armazenar informações sobre vendedores. A tabela deve seguir os conceitos básicos
--de modelo relacional. Certifique-se de definir claramente as colunas da tabela e suas relações
--com outras tabelas, se aplicável.

--8.	Crie uma procedure que insira dados na tabela de vendedores criada anteriormente.
--a.	Validar se o vendedor já existe na tabela.
--b.	Se o vendedor não existir, inserir um novo registro com os dados fornecidos.
--c.	Retornar uma mensagem indicando se a inserção foi bem-sucedida ou se o vendedor já está na tabela.
--		Escreva a implementação completa da procedure, incluindo a validação e a mensagem de retorno.

--9.	Escreva um código em Python que se conecte a um banco de dados SQL Server e chame a procedure criada
--anteriormente para inserir um novo vendedor na tabela criada. Certifique-se de incluir o código de
--conexão ao banco de dados e a chamada da procedure com os parâmetros corretos.

--10.	Em Python, crie um código que carregue em um “data frame” a tabela pedidos e a partir dele retorne
--os 10 produtos mais pedidos com as colunas "productName" e "numberOfOrders" em ordem decrescente.