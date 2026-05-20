from flask import Flask
# Importation de l'extension CORS pour gérer la sécurité des requêtes provenant d'autres origines
from flask_cors import CORS

# Initialisation de l'application Flask
app = Flask(__name__)

# Active CORS sur toute l'application. 
# Cela permet au Front-end (port 9000) d'interroger ce Back-end (port 5252) sans blocage de sécurité
CORS(app)

# Définition de la route '/api/hello' accessible avec la méthode GET par défaut
@app.route('/api/hello')
def hello_world():
    # Renvoie une simple chaîne de caractères qui sera interceptée par le Front-end
    return 'Hello, World!'

# Point d'entrée du script
if __name__ == '__main__':
    # Lance l'application sur toutes les interfaces réseau (0.0.0.0) et sur le port 5252
    app.run(host='0.0.0.0', port=5252)
