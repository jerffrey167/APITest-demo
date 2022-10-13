import requests
#传统表单类POST请求（x-www-form-urlencoded）


url = "https://api.binstd.com/train/station2s"
BodyData = {"start": "天津",
        "end": "北京",
        "ishigh":"0",
        "appkey":"b617c827636c6bb5"
        }
# Post请求发送的数据，字典格式
headers = {"Content-Type: multipart/form-data; boundary=--------------------------522616154642272438893363"}
res = requests.post(url=url, data=BodyData,headers=headers) # 这里使用post方法，参数和get方法一样
print(res.text)
