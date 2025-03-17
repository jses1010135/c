def input_varibles():
    a=float(input("請輸入整數:"))
    print(a)
    b=float(input("請輸入文字:"))
    print(b)
    c=float(input("請輸入文字:"))
    print(c)
    return a,b,c
def main():
    a,b,c=input_varibles()#呼叫函數
    print(a,b,c)
if __name__ == "__main__":#判斷是否為程式的進入點
    main()

