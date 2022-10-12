import  requests

url1 = "https://api.binstd.com/train/station2s?appkey=b617c827636c6bb5&start=天津&end=北京&ishigh=0"
# 参数可以写到url里
res1 = requests.get(url=url1)
print(res1.text)

url2 = "https://api.binstd.com/train/station2s?"
params = {"appkey":"b617c827636c6bb5","start":"天津","end":"北京","ishigh":"0"}
# 字典格式，单独提出来，方便参数的添加修改等操作
res2 = requests.get(url=url2, params=params)
print(res2.text)