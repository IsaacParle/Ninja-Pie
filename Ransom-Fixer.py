import rsa 
import os

files = []

for file in os.listdir():
    if file == "decrypter.py" or file == "encrypter.py" or file == "key_generator.py" or file == "private.pem" or file == "public.pem" or file == "ransom.py" or file == "ransom_fixer.py": 
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

for file in files:
    with open("private.pem", 'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

    with open(file, 'rb') as f:
        data = f.read()


    decrytped_data = rsa.decrypt(data, private_key)


    with open(file, 'wb') as f:
        f.write(decrytped_data)

print("Your files are decrypted")

