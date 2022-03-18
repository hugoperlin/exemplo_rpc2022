from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import uuid
from PIL import Image
from io import BytesIO

from utils import to_byte_array

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths =('/rpc')

def converte_imagem(arg):

    im_file = BytesIO(arg.data)
    im = Image.open(im_file)
    img = im.convert('L')
    
    return xmlrpc.client.Binary(to_byte_array(img))

if __name__ == "__main__":
    
    server = SimpleXMLRPCServer(('localhost',8000),
                                requestHandler=RequestHandler)
    

    server.register_function(converte_imagem,'converter')
    server.serve_forever()

