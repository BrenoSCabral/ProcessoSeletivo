# importando as bibliotecas necessarias
import flask
from flask.json import jsonify

# instanciando a aplicacao para rodar a API
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# criando o objeto para retornar quando for chamado o "hello"
oi = [
  {
    'hello': "Olá, mundo! Sou eu, Breno!"
  }
]

# dando a rota do /hello junto com o metodo a ser executado
@app.route('/hello', methods=['GET'])

# definindo o que a rota /hello vai fazer
def api_hello():
  return jsonify(oi) # transformando o oi definido acima em um JSON e o exportando


# iniciando a aplicação...
app.run()