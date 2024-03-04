# Use a imagem oficial do Node.js
FROM node:16-alpine

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

RUN mkdir node_modules

# Copia os arquivos de código fonte para o contêiner
COPY . .

# Instala o Vue CLI globalmente
RUN npm install -g @vue/cli

RUN npm update -g @vue/cli