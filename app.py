from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Olá, mundo! Esse é meu site. (José Florentino)"

@app.route("/sobre")
def sobre():
  return "Um site muito maneiro. Veja só!"

@app.route("/contato")
def contato():
  return "lucasduartematos@gmail.com"
