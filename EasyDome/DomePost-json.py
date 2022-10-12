#JSON类型的POST请求（application/json）
import json

import  requests

url = "http://120.46.215.163:8101/exam/api/sys/user/login"
data = {
	    "password": "123456",
	    "username": "s2"
        }
headers = {"Content-Type":"application/json"}
# 严格来说，我们需要在请求头里声明我们发送的格式
res = requests.post(url=url, data=json.dumps(data),headers=headers)
#将字典格式的data变量转换为合法的JSON字符串传给post的data参数
print(res.text)