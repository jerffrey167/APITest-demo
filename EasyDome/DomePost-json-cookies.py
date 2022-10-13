#JSON类型的POST请求（application/json）
import json

import  requests

url = "http://120.46.215.163/home-favorites"


cookie= {"PHPSESSID":"lug1q02l2kak6vqjcia0oqdap8"}
res = requests.get(url=url,cookies=cookie)
#将字典格式的data变量转换为合法的JSON字符串传给post的data参数
print(res.text)

