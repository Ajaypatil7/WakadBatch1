import re

# pattern= re.compile("[a-z]")
# matches= re.finditer(pattern, "Bangalore213")
var=input("Enter the Pattern")
mat=re.sub(var,'z', "Bangaloreaaaaaaaaaaaaaaaaaaaa",5)
print(mat)