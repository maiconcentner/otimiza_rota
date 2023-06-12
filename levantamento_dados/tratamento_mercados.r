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

# Criando uma coluna id
base_dados <- base_dados %>%
mutate(id = row_number()) %>%
select(id, everything())

# Removendo endereços duplicados
base_dados_sem_duplicados <- distinct(base_dados, rua, .keep_all = TRUE)

# Somente endereços sem duplicatas
enderecos_sem_duplicados <- base_dados_sem_duplicados$rua
print(enderecos_sem_duplicados)


# Somente enderecos
enderecos_sem <- base_dados_sem_duplicados$rua
print(enderecos_sem)

#salvando lista
write.csv(enderecos_sem, file = "enderecos.csv", row.names = FALSE)

#salvando base de dados completa
write.csv(base_dados_sem_duplicados, file = "base_dados.csv", row.names = FALSE)
