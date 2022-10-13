import requests

url = "http://120.46.215.163:8101"
header ={"Content-Type":"application/json"}
#########################################
Userlogin_api ="/exam/api/sys/user/login"
Userlogin_data = {
	"password": "123456",
	"username": "s2"
		}
login_res = requests.post(url=url+Userlogin_api, json=Userlogin_data,headers=header)
Login_token = login_res.json()["data"]["token"]
print("token:",Login_token)
###############################################
header["token"] = Login_token
#token 赋值
##################################################
Exam_Detail_api="/exam/api/exam/exam/detail"
Exam_Detail_data={"id":"1356425140212076545"}
Exam_Detail_res= requests.post(url=url+Exam_Detail_api,json=Exam_Detail_data,headers=header)
print(Exam_Detail_res.text)
