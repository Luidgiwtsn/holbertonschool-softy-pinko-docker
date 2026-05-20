# Utilise la dernière version stable de Nginx
FROM nginx:latest

# Copie les fichiers statiques du front-end dans le dossier de destination de l'image
COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end

# Remplace la configuration par défaut de Nginx par la nôtre
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf
