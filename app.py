from flask import Flask

app = Flask(__name__)

menu = """
<a href="/">Página Inicial</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a> 

@app.route("/")
def index():
  return "Olá, mundo! Esse é meu site. (Lucas Duarte)"

@app.route("/sobre")
def sobre():
  return "Um site muito paid'égua! Vejam só!"

@app.route("/contato")
def contato():
  return "lucasduartematos@gmail.com"
