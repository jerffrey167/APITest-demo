import requests

url = "http://120.46.215.163:8088"
#########################################
Userlogin_api ="/exam/user.action"
Userlogin_data = {
		"username":"ww",
		"userpwd":"12345"
			}
login_res =requests.post(url=url+Userlogin_api, data=Userlogin_data)

# print(login_res.text)
# print(login_res.cookies)
cookie = login_res.cookies

########################

user_studentPaper_stupaper_api="/exam/user/studentPaper/stupaper.action"

home_favorites = requests.get(url=url+user_studentPaper_stupaper_api,cookies=cookie)
print(home_favorites.text)