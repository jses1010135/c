s0='這是一個字串' # 單引號也可以
s1="這是另一個字串" # 雙引號也可以
s2="這是一個包含'單引號'的字串" # 雙引號也可以
s3='這是一個包含"雙引號"的字串' # 單引號也可以
s4='''這是一個包含'單引號'和"雙引號"的字串''' # 三個單引號也可以
s5="""這是一個
包含
'單引號'
和"雙引號"
的字串
""" # 三個雙引號也可以
print (f"{s0+s1+s2+s3+s4+s5}") # 字串