FROM node:lts-alpine

WORKDIR /app

RUN npm install @vue/cli -g

COPY . .
RUN npm install

RUN ls
CMD ["npm", "run"]