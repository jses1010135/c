def input_variables():
    text = [0] * 5
    for i in range(5):
        text[i] = int(input(f"請輸入第{i+1}個整數: "))
    return text

def compute(text):
    result = (text[1] * text[2] + text[3] / text[4] - text[1])
    return result

def main():
    a = input_variables()
    print(f"({a[1]}*({a[2]}+{a[3]})/{a[4]}-{a[1]})={compute(a)}")

if __name__ == "__main__":
    main()

