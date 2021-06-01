# realizando testes para ver o funcionamento do metodo age

import requests

# o que eu vou passar no post:
dados ={
  'name': 'Breno Cabral',
  'date': '2021-07-07',
  'birthdate': '2021-07-07'
}

r = requests.post('http://127.0.0.1:5000/age', json=dados) # passando
print(r.text) # checando o que ele esta me retornando