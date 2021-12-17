import re

email=input("Enter your mail id")

pat="[\w]+[_\.]*[\w]+@[a-z0-9]+.[a-z]{2,3}"

res=re.match(pat, email)
if res!=None:
    print(res)
    print("it is valid mail id")
else:
    print("Invalid Email Id")