import re
pat=re.compile("[^\w]")
res=re.finditer( pat,"Bang123#$LORE456@Abc",)

print(res)

for i in res:
    print(i.start(), "--->", i.end(), "--->", i.group())