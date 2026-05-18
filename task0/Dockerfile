# Base de l'image sur la dernière version d'Ubuntu
FROM ubuntu:latest

# Mise à jour des dépôts d'APT
RUN apt-get update

# Mise à jour des paquets installés (-y pour répondre "oui" automatiquement)
RUN apt-get upgrade -y

# Commande par défaut pour afficher le message
CMD ["echo", "Hello, World!"]
