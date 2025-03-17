def coculate():
    text=[0]*9
    for i in range(9):
        text[i]=int(input(f"請輸入第{i+1}個整數: "))
    
    return text
def compute(text):
    text1=(text[1]*text[2]-text[3]*text[4]/text[5]*text[6]-text[7]*text[1])
    text2=(text[1]*text[6]-text[3]*text[5]/text[4]*text[7]-text[5]*text[2])
    return text1,text2
def main():
    text=coculate()
    text1,text2=compute(text)
    print(f"x={text1}\ny={text2}")
    
if __name__=="__main__":
    main()