import requests

dados ={
  "name": "Breno Cabral",
  "birthdate": '2000-07-20',
  "date":'0200-09-20'
}

r = requests.post('http://127.0.0.1:5000/age', json=dados)
print(r.text)