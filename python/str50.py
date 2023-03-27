# Program for reversed all the string
# def rev(tem):
#    return tem[::-1]

# def reversed_tem(str):
#     tems=""
#     s=str.split()
#     for i in s:
#         tems=tems+rev(i)+" "
#     print(tems)
# reversed_tem(str="this is the best way to learn")


# WAP for check the string divisible by 7 or not
# def fun(n1):
#     number=int(n1)
#     if number%7==0:
#         print("yes str is dev by 7 ")
#     else:
#      print("no not div by 7")
# def div(str):
#     n=""
#     for i in str:
#         n =n+i 
#     fun(i)
# div(str="777788888")





# WAP for multiply of two string
# def mul(x,y):
#     num1=int(x)
#     num2=int(y)
#     return num1*num2
# s=mul("11","23")
# print(f"mul of 11*23 is {s}")





# def findMinSum(num):
# 	sum = 0
# 	i = 2
# 	while(i*i  <= num):
# 		while(num % i == 0):
# 			sum = sum + i
# 			num = num // i
# 		i += 1
	
# 	if  num ==1:
# 		return sum
# 	else:
# 		sum = sum+num
# 		return sum
# # num =20
# # for i in range(num):
# print (findMinSum(13))




# num = int(input("inter a number : "))
# for i in range(2,int(num/2)+1):
# 	if num % i ==0:
# 		print(num, "is not a prime number")
# 		break		
# else:
# 	print(num, "is a prime number")
	



# def addToList(val, list=[]):
# 	list.append(val)
# 	return list
# list1 = addToList(1)
# list2 = addToList(123)
# list3 = addToList("a",[])


# print ("list1 = %s" % list1)

# print ("list2 = %s" % list2)

# print ("list3 = %s" % list3)







# s="kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm"
# l = len(s)
# n = 75656
# res = ""
# while n>0:
#     for i in s:
#         if n==0:
#             break
#         res = res+i
#         n-=1
            
# print(res.count("a"))


# s = "haveaniceday"
# o ="hae and via ecy"
# n =len(s)
# a= int(n**0.5)
# b= a+1
# list1 = [],[],[],[]
# c = 0
# for j in range(a):
#     for i in range(b):
#         list1[i].append(s[c])
#         c +=1
# print(list1)  

# [ha][an][vi][ec]
# s = "aaabAdddDNH5Q"
# l = []
# for i in range(len(s)):
#     l = l+[s[i]]
# i = 0
# n =len(l)
# while i<n:
#     if i >=n//2:
#         break
#     if l[i]==l[i+1]:
#         del l[i:i+2]
#     else:
#         i = i+1
#     print(''.join(l))
# ct =0    
# for i in s:
#      if i.isupper():
#         ct +=1
# print(ct)
# ps ="HackerRank"
# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_characters = "!@#$%^&*()-+"
# for i in ps:
#     n_bool = 1
#     l_bool = 1
#     u_bool = 1
#     s_bo = 1
# n


# def caesarCipher(s, k):
#     # Write your code here
#     special_characters = "!@#$%^&*()-+"
#     upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     alf = "abcdefghijklmnopqrstuvwxyz"
#     res = ""
#     for i in s:
#         if i in special_characters:
#             res = res+i
#         elif i in upper_case:
#             v =upper_case.index(i)
#             r  = v+k
#             if r >25:
#                 r = r-25
#                 res = res+upper_case[r-1]
#             else:
#                 res = res+upper_case[r]
#         elif i in alf:
#             v =alf.index(i)
#             r  = v+k
#             if r >25:
#                 r = r-25
#                 res = res+alf[r-1]
#             else:
#                 res = res+alf[r]
#     return res

# print(caesarCipher("D3q4",0))


# s= "SOSSOT"
# a ="SOS"
# r =""
# j = 0
# c = 0
# for i in s:
#     r = r+i
#     j +=1
#     if j%3==0 and len(s)>j:
#         r =r+"/"
# res = r.split("/") 
# for i in res:
# 	if i !=a:
# 		for k in range(3):
# 			if i[k]!=a[k]:
# 				c +=1

# print(c)





# def frgh(s):
# 	tem = "hackerrank"
# 	p = 0
# 	res = ""
# 	for i in range(len(tem)):
# 		if i < 9:
# 			p = s.find(tem[i], p) +1
# 			print(p)
# 			res= res+s[i]
# 			if p == 0:
# 				break
# 	print(res)         
# 	if i == 9:
# 		return("YES")
# 	else:
# 		return("NO")
# s= "hereiamstackerrank"
# print(frgh(s))


# def pangrams(s):
#     # Write your code here
# 		a = "abcdefghijklmnopqrstuvwxyz"
# 		A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		
# 		ct = 0
# 		for i in range(len(a)):
# 			if a[i] in s or A[i] in s:
# 				ct += 1
# 		print(ct)
# 		if ct == 26:
# 			return "pangram"
# 		else:
# 			return "not pangram"

# print(pangrams("qmExzBIJmdELxyOFWv LOCmefk TwPhargKSPEqSxzveiun"))


# from collections import Counter
# list = []
# s = "abccddde"
# alf =[abcdefghijklmnopqrstuvwxyz]

# for i in s:
#     list.append((alf.index(i))+1)
        

# print(list)
# a1 = [1,2,5]
# a2 = [1,2,7]
# a3 = []
# i = 5
# for i in range(len(a1)):
#     if a1[i] != a2[i]:
#         a3 = [i]
#         a3.append(a2[i])
# print(a3)
# a1= a1+a2
# a1.sort(reverse=True)
# print(a1)



# s = "NNaAsB"
# r = ""
# for i in s:
#     if i.islower():
#         r= r+i.upper()
#     elif i.isupper():
#         r = r+i.lower()
#     else:
#         r = r+i

# print(r)
# def asd():
#     first = 2
#     last = 3

#     return f"Hello {first} {last}! You just delved into python."
# print(asd())
# s = "asdfghjk55ddd"
# res = ""
# for i in range(len(s)):
#     if i==2:
#         res = res+"\n"
#         res =res+s[i]
#     else:
#         res =res+s[i]

# p = 1 
# d =55
# m = 1
# s =10000

# def howManyGames(p, d, m, s):
#     # Return the number of games you can buy
#     ct =0
#     add = 0
#     for i in range(s):
#         add +=p
#         # print(add)
        
#         if add >=s:
#             ct +=1

#             break
#         elif p >m:
#             p = p-d

#         else:
#             p = p=m
#         ct +=1
        
        
#     return ct

# print(howManyGames(p,d,m,s))



# h= 3
# m =15

# def timeInWords(h, m):
#     # Write your code here
#     time = ["o' clock","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]
#     if m==0:
#         return(f"{time[h]} {time[m]}")
#     elif m >0 and m<20 and m!=15:
#         return(f"{time[m]} minutes past {time[h]}")
#     elif m==15:
#         return(f"quarter past {time[h+1]}")
#     elif m==30:
#         return(f"half past {time[h+1]}")
#     elif m==45:
#         return(f"quarter to {time[h+1]}")
#     elif m >30 and m !=45:
#         return(f"{time[60-m]} minutes to {time[h+2]}")


# print(timeInWords(h,m))





#  n=1
# r=5
# def nCr(n, r):
#     return (fact(n) / (fact(r)* fact(n - r)))*2
# def fact(n):
#     if n == 0:
#         return 1
#     res = 1
#     for i in range(2, n+1):
#         res = res * i
#     return res

# nCr(n, r)
# from collections import Counter
# b = "B_RRBR"

# def happyLadybugs(b):
#     # Write your code here
#     ct = 0
#     ct1=0
#     n = len(b)
#     f = Counter(b)
#     for i in f.values():
#         ct1+=1
#         if i>=2:
#             ct+=1
#     if ct == (ct1-1) and ct1 !=3:
#         print("Yes")
#     else:
#         print("no")
# happyLadybugs(b)





# def beautifulBinaryString(b):
#     # Write your code here
#     ss = "010"
#     ct = 0
#     j = 3
#     k =0
#     for i in range(1,(len(b))+1):
#         print(b[k:j])
#         if b[k:j]==ss:
#             ct+=1
#             k = j
#             j = j+3
#         else:
#             k +=1
#             j = j+1

#     return ct


# print(beautifulBinaryString('11101'))


# def isValid(s):
#     # Write your code here
#     list = []
#     for i in set(s):
#         list.append(s.count(i))
#     list.sort()
#     print(list)
#     if list[0] == list[-1] and list[1]==list[-2]:
#         return "YES"
#     else:
#         list[-1] = list[-1]-1
#         if list[0] == list[-1] and list[0]==list[-2]:
#             return "YES"
#         else:
#             return "NO"

# print(isValid("abcdefghhgfedecba"))


# def candies(n, A):
#     # Write your code here
#     ct = 1
#     list =[1]
#     for i in range(1,n):
#         if A[i-1] <A[i]:
#             ct =(ct+1)
#         elif A[i-1] >=A[i]:
#             if ct>2:
#                 ct= ct-2
#             else:
#                 ct = (ct-1)
#         list.append(ct)
#     print(list)
#     return sum(list)
    
# A = [2,4,2,6,1,7,8,9,2,1]
# n = 10
# print(candies(n,A))
n = 15
# if n <3 :
#     print("-1")
# elif n%3==0:
#     print("5"*n)
# elif n%5==0:
#     print("3"*n)




# def maxMin(k, A):
#     # Write your code here
#     A.sort()
#     l1 = []
#     l2 = []
#     for i in range(len(A)-k+1):
#         l1.clear()
#         for j in range(i,k+i):
#             l1.append(A[j])
#         l2.append(max(l1)-min(l1))
#         print(l2)
#     m = min(l2)
    
#     return m
# k= 3
# A = [100,200,300,350,400,401,402]
# print(maxMin(k,A))

# def jimOrders(orders):
#     # Write your code here
#     t = {}
#     k=[]
#     for i in range(len(orders)):
#         s =(orders[i][0]+orders[i][1])
        
#         t.update({s:i+1})
#     print(t)
       
#     p = sorted(t, key=t.get)
#     print(p)
#     for i in range(len(p)):
#         k.append(t.get(p[i]))
#     print(k)

# orders = [1,1],[1 ,1]
# jimOrders(orders)





# def makingAnagrams(s1, s2):
#     # Write your code here
#     ct = 0
#     a = len(s1)
#     b = len(s2)
    

    
#     for i in set(s1):
#         if i not in s2:
#             ct+=2
#         else:
#             ct +=abs(s1.count(i)-s2.count(i))
#     #  2+2+1+1+2+2+2+2+
        
#     return ct+(b//2)
# s1 = "fcrxzwscanmligyxyvym"
# s2 = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
# print(makingAnagrams(s1,s2
# p = 1
# q = 100
# l = []
# for i in range(4,q+1):

#     sq = i*i
#     res = str(sq)
#     r = len(res)//2

#     r1 = res[:r]
#     r2 = res[r:]
#     if int(r1)+int(r2)==i:
#         l.append(i)
# print(l)
    # else:
    #     for i in res:
    #         res.replace(i,"")    l = []
    
    #     r1 = res[:r]
    #     r2 = res[r+1:]
    #     if int(r1)+int(r2)==i:
    #         
        
    # return l
# def happyLadybugs(b):
#     # Write your code here
#     res = ""
#     ct = 0
#     l =[]
#     for i in b:
#         res+=i
#     for i in range(len(res)):
#         if res[i] =="-":
#             ct +=1
#             res[i].replace("0")
            
#         else:
#             l.append(res.count(res[i]))
#     print(l)
        
#     if l==[] and ct>0:
#         return "YES"
#     else:
#         for i in l:
#             if i==1:
#                 return "NO"
#         else:
#             return "YES"


# print(happyLadybugs("RBY_YBR"))

# def strangeCounter(t):
#     # Write your code here
#     res=3

#     for i in range(1,t):
#         if res==1 and i%3==0:
#             res=3+i
#         else:
#             res -=1

#     return res
# for i in range(1,11):
#     print(strangeCounter(i))



# def absolutePermutation(n, k):
#     # Write your code here
#     l2=[]
#     for i in range(1,n+1):
#         for j in range(n,0,-1):
#             if abs(i-j) ==k:
#                 l2.append(j)
#     # if len(l2)!=n:
#     #     return "no"
#     # else:
#     return l2
    

# print(absolutePermutation(10,3))
# print(bin(4)[2:])
# # sum = bin(int(a, 2) + int(b, 2))
# print(int("100",2))


# def counterGame(n):
#     # Write your code here
#     ct = 0
#     i=1
#     while i<10:
#         print(n)
#         if n ==1:
#             break
#         elif 2**i ==n:
#             n = n//2
#             ct+=1
#             i=1
#         elif 2**i > n:
#             n = n-(2**(i-1))
#             ct+=1
#             i=1
#         else:
#             i+=1
            
#     if ct%2==0:
#         return   "Richard"   
        
#     else:
#         return  "Louise"  
        
# print(counterGame(132))



# def balancedSums(A):
#     # Write your code here
#     for i in A:
#         if sum(A)-i ==0:
#             return "YES"
#     for i in range(1,len(A)-1):
#         print(sum(A[:(i)]) , sum(A[(i+1):]))
#         # if sum(A[:(i-1)]) == sum(A[(i+1):]):
#         #     return "YES"
#     # else:
#     #     return "NO"

# A = [1 ,2 ,3 ,3]
# print(balancedSums(A))

# b ="X_Y__X"
b="RBY_YBR"
# b="__"

# b = "B_RRBR"

# def happyLadybugs(b):
#     # Write your code here
#     res = ""
#     ct =0
#     for i in b:
#         if i!="_":
#             res = res+i
#         else:
#             ct+=1
#     if res =="" and ct >0:
#         return "YES"      
#     for i in res:
#         print(res)
#         print(res.count(i))
#         if res.count(i)==1:
#             return "NO"
            
        
#     return "YES"
# print(happyLadybugs(b))


def almostSorted(arr):
    # Write your code here
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                a = i
                print(arr[a])
                for k in range(i+1,len(arr)):
                    # if arr[k]>arr[a]:
                    #     arr[k-1],arr[a]=arr[a],arr[k-1]
                    #     if arr == arr.sort():
                    #         return "yes"
                    if arr[k]>arr[a]:
                        arr[:4].sort()
                        print(arr)
                        if arr == arr.sort():
                            return "yes","reverse"
print(almostSorted([1, 5, 4, 3 ,2 ,6]))