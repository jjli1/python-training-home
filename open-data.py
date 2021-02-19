# import urllib.request as request
# src="https://www.ntu.edu.tw"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8")

# print(data)

import urllib.request as request
import json

src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response)
clist=data["result"]["results"]
# for company in clist:
#     print(company["公司名稱"])
with open("data.txt","w",encoding="utf-8") as file:
    for company in clist:
        print(company["公司地址"],company["公司名稱"])
        file.write(company["公司名稱"]+"\t"+company["公司地址"]+"\n")