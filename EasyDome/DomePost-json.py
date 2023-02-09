#JSON类型的POST请求（application/json）
import json

import  requests

url = "http://120.46.215.163:8102/exam/api/sys/user/login"
data = {
	    "password": "123456",
	    "username": "s2"
        }
# 字典格式，方便添加和修改
headers = {"Content-Type":"application/json"}
# 严格来说，我们需要在请求头里声明我们发送的格式

#将字典格式的data变量转换为合法的JSON字符串传给post的data参数
#res = requests.post(url=url, data=json.dumps(data),headers=headers)

res = requests.post(url=url,json=data,headers=headers)
#将字典格式的data变量直接作为JSON字符串传给post的json参数
print(res.text)
