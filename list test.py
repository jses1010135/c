mylist = [1,2,3,4,5] # 串列
mylist.append(6) # 串列新增元素
mylist.remove(6) # 串列刪除元素
mylist.insert(0,0) # 串列插入元素
mylist.pop(0) # 串列取出元素
mylist.sort() # 串列排序
mylist.reverse() # 串列反轉
mytuple = (1,2,3,4,5) # 元組
myset = {1,2,3,4,5} # 集合
mydict = {'a':1,'b':2,'c':3} # 字典

print (f"mylist={mylist}") # 串列
print (f"mytuple={mytuple}") # 元組
print (f"myset={myset}") # 集合
print (f"mydict={mydict}") # 字典
print (f"mylist[0]={mylist[0]}") # 串列索引
print (f"mytuple[0]={mytuple[0]}") # 元組索引
print (f"myset={myset}") # 集合
print (f"mydict['a']={mydict['a']}") # 字典索引
print (f"mydict.get('a')={mydict.get('a')}") # 字典索引
print (f"mydict.get('d')={mydict.get('d')}") # 字典索引
print (f"mydict.get('d','沒有這個鍵')={mydict.get('d','沒有這個鍵')}") # 字典索引