import requests
url = "https://newsapi.org/v2/everything"

params = {
    "q": "спорт",
    "language":"ru",
    "sortBy":"popularity",
    "from": "2025-02-15",
    "apiKey": "a115a0b9170b4ff79fc191a26418eebd",
    "pageSize": 5
}

my_api = requests.get(url, params = params,).json()


for i in range(5):
    print(f"{my_api.get('articles')[i].get('title')}. Источник: "
          f"{my_api.get('articles')[0].get('source').get("name")}", end ="\n"*2)
