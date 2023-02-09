import requests

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
print("token:",Login_token)
###############################################
header["token"] = Login_token
#token 赋值
##################################################
Exam_online_paging_api="/exam/api/exam/exam/online-paging"
Exam_online_paging_data={
						"current":"1",
						 "size":"10",
	 					"params":"",
						 "t":"1664197427420"
						 }

Exam_online_paging_res= requests.post(url=url+Exam_online_paging_api,json=Exam_online_paging_data,headers=header)
print(Exam_online_paging_res.text)

ExamTitle = Exam_online_paging_res.json()["data"]["records"][1]["title"]

print(ExamTitle)