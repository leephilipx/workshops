import requests

endpoint_url = 'YOUR_ENDPOINT_URL_HERE'
query = { "data": "5.1, 3.8, 1.6, 0.2" }

response = requests.post(endpoint_url, json=query)

print(response.json())