import requests
#传统表单类POST请求（x-www-form-urlencoded）


# url = "https://api.binstd.com/train/station2s"
# data = {"start": "天津",
#         "end": "北京",
#         "ishigh":"0",
#         "appkey":"b617c827636c6bb5"
#         }
# # Post请求发送的数据，字典格式
# headers = {"Content-Type: multipart/form-data;"}
# res = requests.post(url=url, data=data) # 这里使用post方法，参数和get方法一样
# print(res.text)



url2 = "http://120.46.215.163/shop-cart/add"
data2 = {
        "goodsId":"7",
        "buyNum":"1"
        }
headers2 = {"Content-Type":"application/x-www-form-urlencoded;"}
cookies =  {"PHPSESSID":"8lofdu6tj3tp0g6vc1jjf9rvmj"}
res2 = requests.post(url=url2,data=data2,headers=headers2,cookies=cookies)

print(res2.text)