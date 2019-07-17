import json
data='''
[
{"id":"001",
"x":"2",
"name":"chuck"
}
]'''
info=json.loads(data)
print('User count:',len(info))
for item in info:
    print("name:",item["name"])
        
