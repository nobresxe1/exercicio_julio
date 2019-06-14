import requests
import json
import hashlib
request = requests.get(
    'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=255b15e05d67a93b16baa5f9be2fe493074d388e')
resposta = request.json()
arquivo = open('answer.json', "w")
json.dump(resposta, arquivo)
arquivo.close()
msg = resposta['cifrado']
s = ''

for c in msg:
    if chr(ord(c)).isidentifier():

        if (ord(c) - resposta['numero_casas']) < 97:
            s += chr(ord(c) - resposta['numero_casas'] + 26)
        else:
            s += chr(ord(c) - resposta['numero_casas'])
    else:
        s += chr(ord(c))

dados = {
    'numero_casas': resposta['numero_casas'],
    'token': resposta['token'],
    'cifrado': resposta['cifrado'],
    'decifrado': s,
    'resumo_criptografico': hashlib.sha1(s.encode()).hexdigest()
}

arquivo = open('answer.json', "w")
json.dump(dados, arquivo)
arquivo.close()

url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=255b15e05d67a93b16baa5f9be2fe493074d388e'
files = {'answer': open('answer.json', 'rb')}
r = requests.post(url, files=files)
r.text