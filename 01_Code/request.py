import requests

url = 'http://127.0.0.1:5000/predict_api'
r = requests.post(url,json={'job':"machine learning engineer"})

print(r.json())