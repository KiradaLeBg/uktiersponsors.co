import requests as re
import json

url = 'https://uktiersponsors.co.uk/tierApi/api/tierData/Companies'
page = 1
path = r"C:\Users\wyzix\OneDrive\Bureau\Spider\data.json"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": "70",
    "Content-Type": "application/json",
    "Cookie": "_ga=GA1.3.925513323.1690134936; _gid=GA1.3.492608755.1691172202",
    "Host": "uktiersponsors.co.uk",
    "Origin": "https://uktiersponsors.co.uk",
    "Referer": "https://uktiersponsors.co.uk/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
}

payload = {
    "PageNumber": page,
    "RowsPerPage": 20,
    "Company": "",
    "Town": "",
    "Industry": ""
}

details = []

while page <= 3577:
    a = re.post(url, headers=headers, json=payload)
    if a.status_code == 200:
        data = a.json()
        companies = data.get("companies", [])
        for i in companies:
            details.append(i)
        with open(path, "a") as files:
            json.dump(details, files, indent=4)
            files.write("\n")
        page += 1
    else:
        print(f"error, response code : {a.status_code}")
        break
