import requests
import unittest


class Test_API(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global baseurl,headers
        baseurl = 'http://120.46.215.163:8102'
        headers = {"Content-Type": "application/json"}

    def test_001login(self):
        data = {"username": "admin", "password": "admin"}
        r = requests.post(url=baseurl+"/exam/api/sys/user/login", headers=headers, json=data)
        global token
        token = r.json()["data"]["token"]
        msg = r.json()["msg"]
        self.assertEqual(msg,"操作成功！")


    def test_002UploadFile(self):
        files_qu = [
            ('file', ('123.xlsx', open('C:/Users/jerffrey/Downloads/123.xlsx', 'rb')))
        ]
        header_import = {"token": ""}
        header_import["token"] = token
        r = requests.post(url=baseurl+"/exam/api/qu/qu/import", headers=header_import, files=files_qu)
        msg = r.json()["msg"]
        self.assertEqual(msg,"请求成功！")

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()