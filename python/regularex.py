import re
txt = "The twenkel twenkel little star"
x = re.search("^The.+star$", txt)
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

x = re.findall("el", txt)
print(x)