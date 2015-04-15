lis=[]
i=1
while i<=10:
	name=raw_input('name:')
	if name not in lis:
		lis.append(name)
	i+=1
print lis


##No.2
omit = False
for line in open("a.txt"):
    if line == "#start\n":
        omit = True
    elif line == "#end\n":
        omit = False
    else:
        if not omit: print line[:-1]
#去除某列：

fileObject = open("data.csv")
res = list(fileObject)
new = [res[0]]
i = 1
while i < len(res):
    temp = int((res[i].split(","))[3].strip("\n"))
    if temp < 0 or temp >=5:
        i += 1
        continue
    new.append(res[i])
    i += 1

fileObject1 = open("newdata.csv", "w")
fileObject1.writelines(new)
fileObject1.close()
fileObject.close()

去除某行：
for line in open("a.txt"):
    if not re.match("123456", line):
           line[:-1]  

import re

list = []                              
matchPattern = re.compile(r'.+:\sdana') #简陋的reg用来匹配包含'dana'的那行
file = open('source.txt','r')           #假设'source.txt'是你要处理的文档
while 1:
    line = file.readline()              #从文件中读出一行
    if not line:                        #如果读出的是文件结尾，就退出循环
        break
    elif matchPattern.search(line):     #如果读出的行匹配上了定义的reg,那啥也不做
        pass
    else:                               #如果读出的行不匹配reg,也不是文件尾，那就
        list.append(line)               #把这行存入list列表。
file.close()

file = open('target.txt', 'w')         #重新打开一个文件，把list列表里面的内容   
for i in list:                         #逐行写入。最后'target.txt'文件就是不包含
    file.write(i)                      #'dana'那行的文件
file.close()        
