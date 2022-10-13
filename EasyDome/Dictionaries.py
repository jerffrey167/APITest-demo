
###################
# #python字典与json
###################
import   json


################python字典的生成
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

################################
#Python的字典和JSON在表现形式上非常相似
#Python中的一个字典
dic = { 'str': 'this is a string',
        'list': [1, 2, 'a', 'b'],
        'sub_dic': { 'sub_str': 'this is sub str',
                     'sub_list': [1, 2, 3] },
                    'end': 'end' }
#JSON对象
json_obj = { 'str': 'this is a string',
             'arr': [1, 2, 'a', 'b'],
             'sub_obj': { 'sub_str': 'this is sub str',
                          'sub_list': [1, 2, 3] },
             'end': 'end' }
###############################














