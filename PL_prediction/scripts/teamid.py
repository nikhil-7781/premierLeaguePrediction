import requests, json

url='https://livescore-api.com/api-client/leagues/table.json?competition_id=2&key=2O4NK7SsaREzVlj3&secret=PqXIrAwgyGMznJuqyzdiG5KRXprTLKWA'
response = requests.get(url)
data = response.json()

print(json.dumps(data, indent=2))