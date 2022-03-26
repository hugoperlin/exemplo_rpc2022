import xmlrpc.client, os
from PIL import Image
from io import BytesIO

from utils import to_byte_array

PATH = os.getcwd() + "/src/imgs/"

if __name__ == "__main__":
    client = xmlrpc.client.ServerProxy("http://localhost:8000/rpc")

    img = Image.open(PATH + "img.jpg")

    resp = client.converter(xmlrpc.client.Binary(to_byte_array(img)))

    im_file = BytesIO(resp.data)
    im = Image.open(im_file)
    im.save(PATH + "ret.png")
