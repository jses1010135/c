text=int(input("請輸入整數:"))
print(text)
text1=float(input("請輸入文字:"))
print(text1)
# text2=eval(input("請輸入文字:")) #轉成任何型態
# print(text2)

#基本輸出
# print("輸出的","\t","a",end="\n")#end=""不換行
# print(end="\n")#換行
# print("輸出的","\t","b",end="\n")#end="\n"換行

#常用的跳脫字元
# print()#換行
# print("a,b")#逗號會自動加空格
# print("a, b")
# print("\b")#退格
# print("\f")#換頁
# print("\n")#換行
# print("\r")#歸位
# print("\t")#水平定位
# print("\v")#垂直定位
# print("\a")#響鈴
# print("\'")#單引號
# print("\"")#雙引號
# print("\\")#反斜線
# print("\0")#空字元

#格式化輸出
# print("這是整數%4d,這是浮點數%4f,這是16進制%x,八進制%o" %(text,text1,text,text))
# print("a=%d" %text)#整數
# print("a=%f" %text1)#浮點數
# print("a=%s" % "abc")#字串
# print("a=%x" % 10)#16進位
# print("a=%o" % 10)#8進位
# print("a=%e" % 100)#科學記號
# print("a=%g" % 100)#自動選擇整數或科學記號
# print("a=%c" % 97)#字元
# print("a=%r" % "abc")#字串
# print("%-10d" % 10)#靠左對齊
# print("%10d" % 10)#靠右對齊
# print("%010d" % 10)#補0
# print("%+d" % 10)#正負號

#格式化位置輸出
print("a={0},b={1}".format(10,20))#舊版位置
print("a={1},b={0}".format(10,20))
print("a={0},b={0}".format(10,20))
print("a={a},b={b}".format(a=10,b=20))
print("a={},b={}".format(text,text1))
print(f"a={10},b={20}")#新版位置
