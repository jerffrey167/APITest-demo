import requests
import unittest


class Test_API(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global baseurl,headers
        baseurl = 'http://120.46.215.163:8102'
        headers = {"Content-Type": "application/json"}

    def test_006login(self):
        data = {"username": "admin", "password": "admin"}
        r = requests.post(url=baseurl+"/exam/api/sys/user/login", headers=headers, json=data)
        global token
        token = r.json()["data"]["token"]
        msg = r.json()["msg"]
        self.assertEqual(msg,"操作成功！")


    def test_007UploadFile(self):
        files_qu = [
            ('file', (open('C:/Users/jerffrey/Downloads/123.xlsx', 'rb')))
        ]

        if token !={"ddddd4444444"}:
            self.skipTest("token 不正确不能上传")
        header_import = {"token": ""}
        header_import["token"] = token
        r = requests.post(url=baseurl+"/exam/api/qu/qu/import", headers=header_import, files=files_qu)
        msg = r.json()["msg"]
        self.assertEqual(msg,"导入出现问题，行：0，null")

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()