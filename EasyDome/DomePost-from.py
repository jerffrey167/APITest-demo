import requests
#传统表单类POST请求（x-www-form-urlencoded）


url = "https://api.binstd.com/train/station2s"
data = {"name": "hanzhichao",
        "age": 18
        }
# Post请求发送的数据，字典格式
res = requests.post(url=url, data=data) # 这里使用post方法，参数和get方法一样
print(res.text)