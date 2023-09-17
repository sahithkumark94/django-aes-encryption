import base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import json

key = 'tf1EOH1JIEiprTmC'
iv =  'tf1EOH1JIEiprTmC'.encode('utf-8')

class Encrypt:
    
    def __init__(self, json_data, conversion_type):
        if conversion_type == 'json':
            self.data = json.dumps(json_data)
        else:
            self.data = json_data
            
    def encrypt(self):
        plaint_text = self.data
        data= pad(plaint_text.encode(),16)
        cipher = AES.new(key.encode('utf-8'),AES.MODE_CBC,iv)
        encrypted_data = base64.b64encode(cipher.encrypt(data))
        response = {
            "response" : encrypted_data.decode("utf-8", "ignore")
        }
        return response
    
class Decryption:

    def __init__(self, ciphertext):
        self.data = ciphertext

    def decrypt(self):
        enc = self.data
        enc = base64.b64decode(enc)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        decrypted =  unpad(cipher.decrypt(enc),16)
        return decrypted.decode("utf-8", "ignore")
    
def convertToJson(json_data):
        return json.loads(json_data)
    
def responseFormat(status_code, message, exception, data):
    resp = {"status": status_code,
                             "message": message,
                             "exception": exception,
                             "data": data}
    return resp

    

    