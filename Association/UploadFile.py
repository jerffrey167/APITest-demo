import requests
#
# url = "http://120.46.215.163:8102/exam/api/qu/qu/import"
# payload={}
# files=[
#   ('file',('qu-import-template.xlsx',open('C:/Users/jerffrey/Downloads/qu-import-template.xlsx','rb')))
# ]
# headers = {
#   'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzgxNzY3MzYsInVzZXJuYW1lIjoiYWRtaW4ifQ.jA79FwTxDCZFT3zYBqxMfWD_W1MDiOnkndDreCsd1WQ'
# }
# response =	requests.post(url=url, headers=headers,files=files)
# print(response.text)
##################################################################

url = "http://120.46.215.163:8102"
header ={"Content-Type":"application/json"}
#########################################
Userlogin_api ="/exam/api/sys/user/login"
Userlogin_data = {
				"password": "123456",
				"username": "s2"
				}
login_res = requests.post(url=url+Userlogin_api, json=Userlogin_data,headers=header)
Login_token = login_res.json()["data"]["token"]
###############################################
qu_import_api="/exam/api/qu/qu/import"
header_import={"token":""}
header_import["token"] = Login_token
files_qu=[
  ('file',('123.xlsx',open('C:/Users/jerffrey/Downloads/123.xlsx','rb')))
]
qu_import_res = requests.post(url=url+qu_import_api,files=files_qu,headers=header_import)
print(qu_import_res.text)
