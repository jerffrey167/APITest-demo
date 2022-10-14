import requests

url = "http://120.46.215.163/"
#########################################
Userlogin_api ="shop-user"
Userlogin_data = {"shopCsrf":"3004a4f1307daf2829e0f96b177655b4-522dbebcf50dbe1819946f29d6c60e07",
				"loginAccount":"jerffrey",
				"loginPassword":"12345678",
				"httpReferer":""}
login_res =requests.post(url=url+Userlogin_api, data=Userlogin_data)

# print(login_res.text)
# print(login_res.cookies)
cookie = login_res.cookies
########################
shop_home_favorites_api="home-favorites"
home_favorites = requests.get(url=url,cookies=cookie)
print(home_favorites.text)