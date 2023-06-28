import json
import requests

url = "https://**********************shanghai.app.tcloudbase.com/test"
headers = {
    "Content-Type": "application/json"
}
data = {"name": "John Smith",
        "age": 35,
        "action": "register",
        "hobbies": ["reading",
                    "hiking",
                    "traveling"
                    ],
        "userInfo": {"appId": "",
                    "openId": "oaoLb4qz0R8STBj6ipGlHkfNCO2Q"
                    }
        }
data = json.dumps(data)

response = requests.post(url, headers=headers, json=data)
print(response.text)