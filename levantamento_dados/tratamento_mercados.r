# Carregando a biblioteca dplyr
library(dplyr)
library(tidyverse)

# Definindo o diretório de trabalho
setwd("D:\\Mestrado\\1Sem_23\\Otimizacao\\levantamento_dados")

# Carregando a base de dados
dados <- read.csv('lista_mercados.csv', sep = ";", header = FALSE)

# Definindo os nomes das colunas
nome_colunas <- c("nome_mercado","endereco")
colnames(dados) <- nome_colunas

# Armazenando a primeira linha
linha_titulo <- dados[1, ]

# Removendo a primeira linha dos dados
dados <- dados[-1, ]

# Adicionando a linha do título como a primeira linha dos dados
dados <- rbind(linha_titulo, dados)

# Separando a coluna "endereco" em duas colunas
base_dados <- separate(dados, endereco, into = c("rua", "telefone"), sep = "·")


