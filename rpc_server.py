from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from minhasClasses import Pessoa


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths =('/rpc')

def ola(nome):
    return "Olá {}, como vai?".format(nome)


def somadora(x,y):
    return x+y

def adicionaAno(pessoa):
    pessoaX = Pessoa(**pessoa)
    pessoaX.somaAno()
    return pessoaX



if __name__ == "__main__":
    
    server = SimpleXMLRPCServer(('localhost',8000),
                                requestHandler=RequestHandler)
    


    server.register_function(somadora,'somar')
    server.register_function(adicionaAno)
    server.register_introspection_functions()
    server.serve_forever()