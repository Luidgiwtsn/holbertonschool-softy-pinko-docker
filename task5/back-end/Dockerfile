# Utilise la dernière image Ubuntu comme base
FROM ubuntu:latest

# Met à jour les paquets du système et installe Python 3 ainsi que le gestionnaire de paquets pip
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip

# Installe le framework Flask pour Python en forçant le passage de la sécurité Ubuntu
RUN pip3 install flask --break-system-packages

# IMPORTANT : Installe l'extension Flask-CORS pour autoriser les requêtes cross-origin
RUN pip3 install flask-cors --break-system-packages

# Définit le dossier /app comme répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier script api.py de votre machine vers le dossier /app du conteneur
COPY ./api.py /app/api.py

# Commande exécutée par défaut au démarrage du conteneur : lance le serveur Flask
CMD ["python3", "api.py"]
