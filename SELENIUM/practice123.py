def prime(n):
    for i in range(2,int(n/2)+1):
        if n%i ==0:
            print("non prime")
            break

    else:
        print("prime")
prime(15)