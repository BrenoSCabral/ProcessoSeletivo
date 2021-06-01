# importando as bibliotecas necessarias
from logging import info
import re
import flask
from flask.json import request, jsonify
import requests
import json
import datetime #para data

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


# partindo agora para a tarefa da rota/recipe
@app.route('/recipe')

def api_recipe():
  # fazendo a verificação de se há a query e os ingredientes e caso o contrario, retornando para o usuario o aviso do que faltou
  if 'i' and 'q' in request.args:
    ingredients = str(request.args['i'])
    query = str(request.args['q'])
  elif 'i' in request.args:
    return "Por favor insira uma receita válida"
  elif 'q' in request.args:
    return "Por favor insira ingredientes"
  else:
    return "Por favor, insira os ingredientes e a query desejada"
  
  # Tratando os resultados
  parametros = {'i': ingredients, 'q':query} # parametros que eu vou fornecer pra API pra pegar o que quero
  url = "http://www.recipepuppy.com/api" # define o site onde eu vou pegar
  call = requests.get(url,params=parametros) # faz a ligacao com a API do recipe puppy e pede os parametros
  data = json.loads(call.content) # interpreto os dados da ligacao como um JSON
  
  # criando o objeto final que vai ser devolvido
  resultado = [{
    'recipe':query,
    'ingredients':ingredients,
    'results':data['results'][:3] # aqui eu corto em results pois e somente o que me interessa e limito para me retornar somente os 3 primeiros resultados
  }]
  return jsonify(resultado) # transformo o objeto em json e o retornando

# agora para o ultimo exercicio:

@app.route('/age', methods=['POST']) # criando a rota
def api_age():
  if not ('name' and 'birthdate' and 'date') in request.json: # verificando se o usuario enviou os dados no formato desejado e,caso o contrario, indicando a forma ideal de se enviar
    return "Por favor insira os dados conforme a seguinte estrutura: { name: “Nome Sobrenome”, birthdate: yyyy-mm-dd, date: YYYY-MM-DD}"
  
  try: # fazendo a verificacao do formato da data
    nasce = datetime.datetime.strptime(request.json['birthdate'], "%Y-%m-%d")
    data = datetime.datetime.strptime(request.json['date'], "%Y-%m-%d")
  except:
    return ('Por favor insira as datas no formato "yyyy-mm-dd"')
  
  if data < nasce: # verificando se a data inserida eh anterior ao nascimento 
    return "Por favor insira uma data posterior ao seu nascimento"
  elif data < datetime.datetime.today():
    return (data - nasce)

# iniciando a aplicação...
app.run()
