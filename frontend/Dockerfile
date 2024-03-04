# Use a imagem oficial do Node.js
FROM node:16-alpine

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos de código fonte para o contêiner
COPY . .

# Instala o Vue CLI globalmente
RUN npm install -g @vue/cli

RUN npm update -g @vue/cli

# Instala as dependências do frontend
RUN npm install

# # Compila o código do frontend
# RUN npm run build

# Expõe a porta 3000 para acessar o servidor de desenvolvimento do Vue.js
EXPOSE 8080

# Inicia o servidor de desenvolvimento do Vue.js
CMD ["npm", "run", "dev"]