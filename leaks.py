import hashlib
import requests

good = "NOT LEAKED"
bad  = "LEAKED!"

with open("passwords.txt", "r") as passwords:
    check = passwords.read()

    for lines in check.split('\n'):
        if lines != "---":

            hidden = hashlib.sha1(str.encode(lines)).hexdigest()
            hidden_hash = hidden[:5]
            all_hidden = hidden[5:]

            req = (requests.get('https://api.pwnedpasswords.com/range/' + hidden_hash).text).lower().find(all_hidden)

            if req < 1:
                print(lines + " : " + good)
            elif req > 1:
                print(lines + " : " + bad)