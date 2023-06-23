'''
   JSON 변환

   1. json --> 문자열
     import json

     json.dumps(json)

   2.  문자열 -->  json

      json.loads(문자열)
'''

import json

# 1. 문자열 -->  json
s = '{"username":"홍길동","age":20}'
print(s, type(s)) #<class 'str'>

s_json = json.loads(s)
print(s_json, type(s_json)) # <class 'dict'>
print(s_json["username"], s_json["age"])

l_s = "[10,20,30]"
print(l_s, type(l_s))
l_s_json = json.loads(l_s)
print(l_s_json, type(l_s_json))
print(l_s_json[0], l_s_json[1], l_s_json[2])

# 2. json --> 문자열
s_json = {"username":"홍길동","age":20}
print(s_json, type(s_json))
s = json.dumps(s_json)
print(s, type(s))
