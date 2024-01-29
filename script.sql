-- irá apagar qualquer banco de dados existente de mesmo nome
DROP DATABASE IF EXISTS dbpython;
-- cria um novo banco de dados chamado 'dbpython'
CREATE DATABASE dbpython;
-- cria uma tabela 'contatos' sobre este banco de dados
CREATE TABLE dbpython.contatos(
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(255),
email VARCHAR(255),
telefone VARCHAR(255)
) ENGINE = InnoDB;
