def input_variables():
    text=[10]
    text[0]=int(input("請輸入整數:"))
    return text
def conpute(text):
    text[0]=text[1]*(text[2]+text[3])/text[4]-text[1]
    return text[0]
def main():
    a=input_variables()
    print(f"{a[0]}*({a[1]}*({a[2]}+{a[3]})/{a[4]}-{a[1]})={conpute(a)}")
if __name__ == "__main__":
    main()

    