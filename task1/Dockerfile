# Base sur la dernière version d'Ubuntu
FROM ubuntu:latest

# Mise à jour d'APT et des paquets installés
RUN apt-get update && apt-get upgrade -y

# Installation de Python3 et pip3
RUN apt-get install -y python3 python3-pip

# Astuce de l'énoncé si l'environnement Python est managé (indispensable sur les Ubuntu récents)
RUN rm -rf /usr/lib/python*/EXTERNALLY-MANAGED

# Installation de Flask via pip3
RUN pip3 install flask

# Définition du dossier de travail dans le conteneur
WORKDIR /app

# Copie du script api.py depuis le PC vers le dossier /app du conteneur
COPY ./api.py /app/api.py

# Commande pour démarrer le serveur Flask au lancement du conteneur
CMD ["python3", "api.py"]
