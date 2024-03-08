FROM node:latest as build

# Répertoire de travail dans le conteneur
WORKDIR /app

# Clonage du repository contenant l'application React
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/dimq/docker-formation.git

# Déplacer le contenu du frontend dans /app
RUN mv docker-formation/frontend/* .

# Installation des dépendances
RUN npm install

# Construction de l'application React
RUN npm run build

FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
