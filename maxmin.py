a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if(a>b and a>c):
   max_num=a
elif(b>a and b>c):
   max_num=b
else:
   max_num=c
if(a<b and a<c):
    min_num=a
elif(b<a and b<c):
    min_num=b
else:
   min_num=c
print("maximum number among three numbers is:",max_num)
print("minimum number among three numbers is:",min_num)      
