import random
import json

with open('f:/proxy.json') as f:
    proxy_list = json.load(f)
    print(proxy_list)
    print(random.choice(proxy_list[]))
