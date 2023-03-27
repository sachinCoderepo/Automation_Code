import json

f = open('sample2.json')

data = json.load(f)

for i in data["phoneNumbers"]:
	print(i)

# Closing file
f.close()
