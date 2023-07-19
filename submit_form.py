import psycopg2
import re
from flask import Flask, request, url_for
from flask import jsonify


app = Flask(__name__)


# Ici on va configurer la base de données PostgreSQL
db_host = "localhost"
db_name = "stania_register"
db_user = "postgres"
db_password = "9052"
db_table = "stania_users"

@app.route('/', methods=['GET'])
def index():
    with open('form.html', 'r') as f:
        return f.read()


@app.route('/submit_form.py', methods=['POST'])
def submit_form():
    nom = request.form['nom']
    prenom = request.form['prenom']
    email = request.form['email']
    date_naissance = request.form['date_naissance']
    pass_client = request.form['pass_client']

    #Vérification des critères de sécurité du mot de passe

    error_message_maj = "Votre mot de passe doit contenir au moins une majuscule."
    error_message_chiffre = "Votre mot de passe doit contenir au moins un chiffre."
    error_message_carspe = "Votre mot de passe doit contenir au moins un caractère spécial"

    if not re.search(r"[A-Z]", pass_client):
        
        return f'''
            <script>
                alert("{error_message_maj}");
                window.history.back();
            </script>
        '''
    
    if not re.search(r"\d", pass_client):
        return f'''
            <script>
                alert("{error_message_chiffre}");
                window.history.back();
            </script>
        '''
    
    if not re.search(r"[!@#$%^&*()_+\-=[\]{};'\":\\|,.<>/?]", pass_client):
        return f'''
            <script>
                alert("{error_message_carspe}");
                window.history.back();
            </script>
        '''

    

    # Connexion à la base de données PostgreSQL
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )

    # Création d'un curseur pour exécuter les requêtes
    cur = conn.cursor()

    # Insertion des données dans la base de données
    cur.execute("INSERT INTO {} (nom, prenom, email, date_naissance, mot_de_passe) VALUES (%s, %s, %s, %s, %s)".format(db_table), (nom, prenom, email, date_naissance, pass_client))

    # Validation de la transaction
    conn.commit()

    # Fermeture de la connexion à la base de données
    cur.close()
    conn.close()

    return ("bien ouej")

if __name__ == '__main__':
    app.run(host='localhost', port=5500)
