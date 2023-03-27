
def table(n):  
    for i in range(1,11):
        print(n*i)
    while n<10:
        n = (n+1)
        table(n)

table(1)