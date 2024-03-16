from flask import Flask
from app.senhas import secrets_key

# Pagina de configuraçao app Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = secrets_key


from app import routes