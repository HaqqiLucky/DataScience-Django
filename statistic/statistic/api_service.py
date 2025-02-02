import requests

def get_quotes(quote):
    base_url = "https://qapi.vercel.app/api/random"
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else: 
        return {"error" : "Failed to fetch data"}