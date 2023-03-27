try:
    a =2
    b = a/0
    print(b)
except Exception as e:
    print("some error")
    print(e)
   
    
    
finally:
    n= 10
    div = n/2
    print(div)