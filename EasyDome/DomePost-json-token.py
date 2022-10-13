#JSON类型的POST请求（application/json）
import json

import  requests

url = "http://120.46.215.163:8101/exam/api/sys/depart/paging"
data = {"current":1,
		"size":10,
		"params":{"deptName":"后勤"}
		}
# 字典格式，方便添加和修改
headers = {"Content-Type":"application/json",
		   "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjU3MzU2NjMsInVzZXJuYW1lIjoiYWRtaW4ifQ.3vBEiUq2h4cwXzwWB-PXrFXCHxru_la3dZTPAg5cOFo"}
# 严格来说，我们需要在请求头里声明我们发送的格式
res = requests.post(url=url, data=json.dumps(data),headers=headers)
#将字典格式的data变量转换为合法的JSON字符串传给post的data参数
print(res.text)
