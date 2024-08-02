###Teste Técnico - Renato Druciak Regis

DROP TABLE IF EXISTS tb_customers;
CREATE TABLE tb_customers(
	customerId INT IDENTITY(1,1) PRIMARY KEY,
	customerDoc CHAR(14),
	firstName VARCHAR(32),
	lastName VARCHAR(32),
	birthDate DATE
);
-- Criação da tabela de produtos
DROP TABLE IF EXISTS tb_products;
CREATE TABLE tb_products(
    productId INT IDENTITY(1,1) PRIMARY KEY,
    productName VARCHAR(50),
    price DECIMAL(10, 2)
);

-- Criação da tabela de pedidos
DROP TABLE IF EXISTS tb_orders;
CREATE TABLE tb_orders(
    orderId INT IDENTITY(1,1) PRIMARY KEY,
    customerId INT FOREIGN KEY REFERENCES tb_customers(customerId),
    orderDate DATE
);

-- Criação da tabela de itens de pedidos
DROP TABLE IF EXISTS tb_order_items;
CREATE TABLE tb_order_items(
    orderItemId INT IDENTITY(1,1) PRIMARY KEY,
    orderId INT FOREIGN KEY REFERENCES tb_orders(orderId),
    productId INT FOREIGN KEY REFERENCES tb_products(productId),
    quantity INT
);

-- Índices para otimização de consultas
CREATE NONCLUSTERED INDEX ix_customerDoc    ON tb_customers(customerDoc) INCLUDE (customerId);
CREATE NONCLUSTERED INDEX ix_customerId     ON tb_orders(customerId);
CREATE NONCLUSTERED INDEX ix_orderId        ON tb_order_items(orderId);
CREATE NONCLUSTERED INDEX ix_productId      ON tb_order_items(productId);

--- População de dados na tabela de tb_customers
INSERT INTO tb_customers(customerDoc, firstName, lastName, birthDate)
SELECT
    RIGHT('00000000000' + CAST(ABS(CHECKSUM(NEWID())) % 100000000000000 AS VARCHAR), 11) AS customerDoc,
    LEFT(NEWID(), 32) AS firstName,
    LEFT(NEWID(), 32) AS lastName,
    DATEADD(DAY, ABS(CHECKSUM(NEWID())) % 36525, '1906-01-01') AS birthDate
FROM
    (SELECT TOP 1000 ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS r FROM sys.columns) AS Numbers;

-- População de dados na tabela de produtos
INSERT INTO tb_products(productName, price)
VALUES
    ('Notebook', 2100.00),
    ('Smartphone', 1200.00),
    ('Tablet', 800.00),
    ('Headphones', 150.00),
    ('Monitor', 500.00),
    ('Keyboard', 80.00),
    ('Mouse', 40.00),
    ('Printer', 250.00),
    ('Webcam', 100.00),
    ('Speakers', 75.00),
    ('External Hard Drive', 130.00),
    ('USB Flash Drive', 20.00),
    ('Router', 90.00),
    ('Smartwatch', 250.00),
    ('Fitness Tracker', 100.00);

-- População de dados na tabela de pedidos
DECLARE @COUNT INT = 0, @LIM INT = 5
WHILE @COUNT <= @LIM BEGIN
	INSERT INTO tb_orders (customerId, orderDate)
	SELECT
		customerId,
		DATEADD(DAY, ABS(CHECKSUM(NEWID())) % 365, GETDATE()) AS orderDate
	FROM
		tb_customers
	WHERE
		customerId <= (SELECT ABS(CHECKSUM(NEWID())) % 1000)

	SET @COUNT += 1

END
;

-- População de dados na tabela de itens de pedidos
DECLARE @COUNT1 INT = 0, @LIM1 INT = 10
WHILE @COUNT1 <= @LIM1 BEGIN
INSERT INTO tb_order_items (orderId, productId, quantity)
SELECT
    o.orderId,
    p.productId,
    ABS(CHECKSUM(NEWID())) % 5 + 1 AS quantity 
FROM
    tb_orders o
    CROSS JOIN tb_products p
WHERE
    ABS(CHECKSUM(NEWID())) % 10 < 3; 

	SET @COUNT1 += 1
END
;


--################### RESPOSTAS ###################

--1.	Crie uma consulta que retorne apenas o item mais pedido e a quantidade total de pedidos.

select top 1
    tpr.productName as Produto
    ,count(tor.orderItemId) as Quantidade_de_pedidos
from tb_products tpr
left join tb_order_items tor on tor.productId = tpr.productId
group by tpr.productName
order by sum(tor.quantity) desc --quantidade vendida
;

--2.	Crie uma consulta que retorne todos os clientes que realizaram mais de 4 pedidos no último ano em ordem decrescente.
select 
    tbc.customerId
    ,tbc.firstName
    ,tbc.lastName
    --,count(tor.orderId) as Numero_de_pedidos
from tb_customers tbc
left join tb_orders tor on tbc.customerId = tor.customerId
where tor.orderDate >= CONVERT(DATE, DATEADD(YEAR, -1, GETDATE()))
    --YEAR(tor.orderDate) = YEAR(GETDATE()) - 1 -- MESES DO ANO ANTERIOR
group by 
    tbc.customerId
    ,tbc.firstName
    ,tbc.lastName
having count(tor.orderId) > 4
order by count(tor.orderId) desc
;

--3.	Crie uma consulta de quantos pedidos foram realizados em cada mês do último ano.


SELECT
    FORMAT(tor.orderDate, 'yyyy-MM') as Mes
    ,COUNT(tor.orderId) as Numero_de_pedidos
from tb_orders tor
where 
	tor.orderDate BETWEEN DATEADD(DAY, 1, EOMONTH(GETDATE(), -13)) AND EOMONTH(GETDATE(), -1)
group by FORMAT(tor.orderDate, 'yyyy-MM')
order by FORMAT(tor.orderDate, 'yyyy-MM')
;



--4.	Crie uma consulta que retorne APENAS os campos "productName" e "totalAmount" dos 5 produtos mais pedidos.

SELECT top 5
	tpr.productName,
	--sum(toi.quantity) as quantity,
	--tpr.price,
	sum(toi.quantity * tpr.price) as totalAmount
from tb_products tpr
left join tb_order_items toi on toi.productId = tpr.productId
GROUP BY tpr.productName
order by sum(toi.quantity) desc
;

--5.	Crie uma consulta liste todos os clientes que não realizaram nenhum pedido.

SELECT
    tbc.customerId
    ,tbc.firstName
    ,tbc.lastName
from tb_customers tbc
LEFT JOIN tb_orders tor on tor.customerId 	= tbc.customerId
where 
	tor.orderId is null
;


--6.	Crie uma consulta que retorne a data e o nome do produto do último
--pedido realizado pelos clientes onde o customerId são 94, 130, 300 e 1000.
SELECT DISTINCT 
	--tor.customerId,
    tor.orderDate AS Data_ultimo_pedido
    ,tpr.productName AS Produto
FROM
    tb_orders               tor
INNER JOIN tb_order_items   toi ON tor.orderId      = toi.orderId
INNER JOIN tb_products      tpr ON toi.productId    = tpr.productId
WHERE
    tor.customerId IN (94, 130, 300, 1000)
AND tor.orderDate = (SELECT MAX(orderDate)
                     FROM tb_orders 
                     WHERE customerId = tor.customerId)

;

--7.	Com base na estrutura das tabelas fornecidas (tb_order_items, tb_orders, tb_products, tb_customers),
--crie uma nova tabela para armazenar informações sobre vendedores. A tabela deve seguir os conceitos básicos
--de modelo relacional. Certifique-se de definir claramente as colunas da tabela e suas relações
--com outras tabelas, se aplicável.

-- criação da tabela de vendedores
DROP TABLE IF EXISTS tb_sellers;
CREATE TABLE tb_sellers(
	sellerId INT IDENTITY(1,1) PRIMARY KEY,
	sellerDoc CHAR(14) NOT NULL,
	firstName VARCHAR(32) NOT NULL,
	lastName VARCHAR(32) NOT NULL,
    commissionPerc DECIMAL(10, 4) NOT NULL,
    CONSTRAINT UQ_sellerDoc UNIQUE (sellerDoc), -- Restringe sellerDoc para ser unico
    CONSTRAINT CK_commissionPerc CHECK (commissionPerc >= 0 AND commissionPerc <= 0.50) -- Restringe commissionPerc para ser entre 0 e 0.50
);

-- criação da tabela pedidos de vendedores, uma vez que a tabela tb_orders já existe no banco e desta forma podemos relacionar os vendedores com os pedidos
DROP TABLE IF EXISTS tb_order_seller;
CREATE TABLE tb_order_seller(
    sellerOrderId INT IDENTITY(1,1) PRIMARY KEY,
    sellerId INT FOREIGN KEY REFERENCES tb_sellers(sellerId),
    orderId INT FOREIGN KEY REFERENCES tb_orders(orderId)
);

-- Índices para otimização de consultas
CREATE NONCLUSTERED INDEX ix_sellerDoc    ON tb_sellers(sellerDoc) INCLUDE (sellerId);
CREATE NONCLUSTERED INDEX ix_sellerId     ON tb_order_seller(sellerId);
CREATE NONCLUSTERED INDEX ix_orderId      ON tb_order_seller(orderId);

--- População de dados na tabela de tb_customers
INSERT INTO tb_sellers(sellerDoc, firstName, lastName, commissionPerc)
SELECT
    RIGHT('00000000000' + CAST(ABS(CHECKSUM(NEWID())) % 100000000000000 AS VARCHAR), 11) AS sellerDoc,
    LEFT(NEWID(), 32) AS firstName,
    LEFT(NEWID(), 32) AS lastName,
    CAST((0.05 + (ABS(CHECKSUM(NEWID())) % 501) / 10000.0) AS DECIMAL(10,4)) AS commissionPerc
FROM
    (SELECT TOP 5 ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS r FROM sys.columns) AS Numbers;

--8.	Crie uma procedure que insira dados na tabela de vendedores criada anteriormente.

--a.	Validar se o vendedor já existe na tabela.
--b.	Se o vendedor não existir, inserir um novo registro com os dados fornecidos.
--c.	Retornar uma mensagem indicando se a inserção foi bem-sucedida ou se o vendedor já está na tabela.
--		Escreva a implementação completa da procedure, incluindo a validação e a mensagem de retorno.

DROP PROCEDURE IF EXISTS usp_insert_seller;

CREATE PROCEDURE usp_insert_seller
    @sellerDoc CHAR(14),
    @firstName VARCHAR(32),
    @lastName VARCHAR(32),
    @commissionPerc DECIMAL(10, 4)
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        DECLARE @message NVARCHAR(100);-- Variável para armazenar a mensagem de retorno

        -- Verificar se o vendedor já existe
        IF EXISTS (SELECT 1 FROM tb_sellers WHERE sellerDoc = @sellerDoc)
        BEGIN
            SET @message = 'Vendedor já está na tabela.';-- Se o vendedor já existir, envia a mensagem
        END
        ELSE
        BEGIN
            -- Se o vendedor não existir, insere um novo registro
            INSERT INTO tb_sellers (sellerDoc, firstName, lastName, commissionPerc)
            VALUES (@sellerDoc, @firstName, @lastName, @commissionPerc);
            SET @message = 'Inserção bem-sucedida.'; -- Mensagem de retorno para inserção bem-sucedida
        END
        SELECT @message AS Message;-- Retornar a mensagem
    END TRY
    BEGIN CATCH
        SELECT ERROR_MESSAGE() AS ErrorMessage; --Capturar o erro e retornar a mensagem de erro
    END CATCH
END;

--teste da procedure
EXEC usp_insert_seller @sellerDoc = '123123123', @firstName = 'asd', @lastName = 'qwe', @commissionPerc = 7.50;

select * from tb_sellers;



--9.	Escreva um código em Python que se conecte a um banco de dados SQL Server e chame a procedure criada
--anteriormente para inserir um novo vendedor na tabela criada. Certifique-se de incluir o código de
--conexão ao banco de dados e a chamada da procedure com os parâmetros corretos.

#execução docker em wsl2 "sudo docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=YourPassword!' -p 1433:1433 --name sqlserver -d mcr.microsoft.com/mssql/server:2019-latest"

import pymssql

# Função para inserir um novo vendedor

conection_string = {
    'server': 'localhost',
    'user': 'sa',
    'password': 'YourPassword!',
    'database': 'master'
}

vendedor = {
    'sellerDoc': '123456789',
    'firstName': 'João',
    'lastName': 'Silva',
    'commissionPerc': 0.05
}

def mysql_cursor(conection_string):
    try:
        # Conectar ao banco de dados
        conn = pymssql.connect(**conection_string)
        return conn.cursor(), conn
    except pymssql.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None, None


def insert_seller(cursor, conn, sellerDoc, firstName, lastName, commissionPerc):
    try:
        with cursor:
            cursor.callproc('usp_insert_seller', (sellerDoc, firstName, lastName, commissionPerc))
            result = cursor.fetchall()
            for row in result:
                print(row)
        conn.commit()
    except Exception as e:
        print("Erro ao executar a procedure:", e)
        conn.rollback()
    finally:
        conn.close()


if __name__ == "__main__":
    cursor, conn = mysql_cursor(conection_string)
    if cursor and conn:
        insert_seller(cursor, conn, **vendedor)


--10.	Em Python, crie um código que carregue em um “data frame” a tabela pedidos e a partir dele retorne
--os 10 produtos mais pedidos com as colunas "productName" e "numberOfOrders" em ordem decrescente.

import pymssql
import pandas as pd

conection_string = {
    'server': 'localhost',
    'user': 'sa',
    'password': 'YourPassword!',
    'database': 'master'
}

def mysql_cursor(conection_string):
    try:
        # Conectar ao banco de dados
        conn = pymssql.connect(**conection_string)
        return conn.cursor(), conn
    except pymssql.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None, None

def executa_query(cursor, query):
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except pymssql.Error as e:
        print(f"Erro ao executar a query: {e}")
        return None

           
if __name__ == "__main__":
    cursor, conn = mysql_cursor(conection_string)
    if cursor and conn:
        query_orders = "SELECT * FROM tb_order_items"
        data_orders = executa_query(cursor, query_orders)
        df_orders = pd.DataFrame(data_orders, columns=[desc[0] for desc in cursor.description])
            
        query_products = "SELECT * FROM tb_products"
        data_products = executa_query(cursor, query_products)
        df_products = pd.DataFrame(data_products, columns=[desc[0] for desc in cursor.description])
        
        # faz o join entre os dataframes df_orders e df_products
        df = pd.merge(df_orders, df_products, left_on='productId', right_on='productId', how='inner')
        #faz os devidos agrupamentos
        df = df.groupby('productName').agg({'orderItemId': 'nunique','quantity': 'sum'}).reset_index()
        #altera o nome da coluna orderItemId para numberOfOrders, uma vez que a mesma representa a quantidade de pedidos daquele produto
        df.rename(columns={'orderItemId': 'numberOfOrders'}, inplace=True)
        #ordena a quantidade vendida em ordem decrescente
        df = df.sort_values(by='quantity', ascending=False)
        #manter apenas o top 10 em quantidade vendida no data frame
        df = df[['productName', 'numberOfOrders']].head(10)
        #reordena o dataframe de acordo com a coluna numberOfOrders em ordem decrescente
        df = df.sort_values(by='numberOfOrders', ascending=False)
        #retorna os 10 produtos mais pedidos com as colunas "productName" e "numberOfOrders" em ordem decrescente.
        print(df)




