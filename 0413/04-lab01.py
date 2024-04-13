import random as rd

strData = ""
answer = rd.randint(1, 100)

while True:
    indata = int(input("1 ~ 100 사이의 수를 입력 : " if strData == "" else strData))
    if indata == answer:
        print(f"축하한다. {indata}: 정답이다.")
        break
    strData = f"{indata}보다 더 {("큰" if indata < answer else "작은")} 수로 다시 입력 : "
print(" 종료 ".center(30, "="))
