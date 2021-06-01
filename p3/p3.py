# importando as bibliotecas necessarias para fazer a API rodar
import flask
from flask.json import request, jsonify
import requests
import json
import datetime #para data
import math # para descobrir o ano no ultimo exercicio

# instanciando a aplicacao para rodar a API
app = flask.Flask(__name__)
app.config["DEBUG"] = True

######################################################################################################################################
######################################################### rota /hello ################################################################
#####################################################################################################################################

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

#####################################################################################################################################
###################################### partindo agora para a tarefa da rota/recipe ##################################################
#####################################################################################################################################

@app.route('/recipe')

def api_recipe():
  # fazendo a verificação de se há a query e os ingredientes e caso o contrario, retornando para o usuario o aviso do que faltou
  if 'i' and 'q' in request.args:
    ingredients = str(request.args['i'])
    query = str(request.args['q'])
  elif 'i' in request.args:
    return "Por favor insira uma receita válida."
  elif 'q' in request.args:
    return "Por favor insira ingredientes."
  else:
    return "Por favor, insira os ingredientes e a query desejada."
  
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

#####################################################################################################################################
############################################# agora para o ultimo exercicio #########################################################
#####################################################################################################################################

@app.route('/age', methods=['POST']) # criando a rota
def api_age():
  # verificando se o usuario enviou os dados no formato desejado e,caso o contrario, indicando a forma ideal de se enviar
  if not 'name'  in request.json or not 'birthdate' in request.json or not 'date' in request.json:
    return "Por favor insira os dados conforme a seguinte estrutura: { name: “Nome Sobrenome”, birthdate: yyyy-mm-dd, date: YYYY-MM-DD}."
  
  try: # fazendo a verificacao do formato da data
    data_nasc = datetime.datetime.strptime(request.json['birthdate'], "%Y-%m-%d")
    data_futuro = datetime.datetime.strptime(request.json['date'], "%Y-%m-%d")
  except:
    return ('Por favor insira as datas no formato "yyyy-mm-dd"')
  
  if data_futuro < datetime.datetime.today(): # verificando se a data inserida e no futuro 
    return "Por favor insira uma data no futuro."
  elif data_nasc > datetime.datetime.today(): # verificando se a data de nascimento e no futuro
    return "Por favor, insira uma data de nascimento no passado."
  else:
    dif_data_futuro = data_futuro - data_nasc # vendo a diferenca da data futura com a data de nascimento
    idade_futuro = math.floor(dif_data_futuro.days/365) # convertendo essa diferenca para anos

    dif_data_hoje = datetime.datetime.today() - data_nasc # vendo a diferenca da data de hoje com a de nascimento
    idade_hoje = math.floor(dif_data_hoje.days/365) # convertendo essa diferenca para anos

    # criando o objeto que vou retornar 
    info = {
    'quote': "Olá, " + request.json['name']+ "! Você tem " + str(idade_hoje) + " anos e em " + datetime.datetime.strftime(data_futuro, "%d/%m/%Y") + " você terá " + str(idade_futuro) + " anos.",
    'ageNow': idade_hoje,
    'ageThen': idade_futuro
    }

    return jsonify(info) # finalmente o retornando!

# iniciando a aplicação...
app.run()
