# t1 = (2,5,7,8)
# t2 = (1,2,3,4)
# print(t1 + t2)

# import numpy as np
# n1 = np.ones((5,5))
# print(n1)

import requests

req = requests.get("https://reqres.in/api/users?page=2")
print(req)
code = req.status_code
print(type(req))
print(dir(req))
print(code)
assert code == 200, "code does not match"

print(req.text)
print(req.content)
print(req.json)
print(req.url)