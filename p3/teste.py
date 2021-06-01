# realizando testes para ver o funcionamento do metodo age
import requests

r1 = requests.get('http://127.0.0.1:5000/hello') # vendo o que me retorna da api /hello
print (r1.text) # checando o resultado

r2 = requests.get('http://127.0.0.1:5000/recipe?i=chocolate&q=cake') # vendo o que me retorna da api /recipe com ingrediente e query genericos
print (r2.text) # checando o resultado

# o que eu vou passar no post:
dados ={
  'name': 'Breno Cabral',
  'date': '2021-07-07',
  'birthdate': '2000-07-07'
}

r3 = requests.post('http://127.0.0.1:5000/age', json=dados) # passando
print(r3.text) # checando o que ele esta me retornando