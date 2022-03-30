import xmlrpc.client
from minhasClasses import Pessoa

if __name__ == "__main__":
    client = xmlrpc.client.ServerProxy("http://localhost:8000/rpc")
    pessoa = Pessoa("ze", 23)
    pessoa2 = client.adicionaAno(pessoa)
    pessoa2 = Pessoa(**pessoa2)
    print(pessoa2.idade)
    # print(client.somar(10, 15))
