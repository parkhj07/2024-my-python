print(divmod(15, 4))
print(15 // 4, 15 % 4)
print("파이썬!!!")

# %%
print(bin(1), bin(10), bin(20))
print(oct(1), oct(20), oct(20))
print(hex(1), hex(10), hex(20))
# %% 2-15base.py
# data = input("정수 입력 >> ") error!
data = int(input("정수 입력 >> "))

print(f"2진수 : {bin(data)}")
print(f"8진수 : {oct(data)}")
print(f"10진수 : {data}")
print(f"16진수 : {hex(data)}")
# %% 두 수의 합 출력
data = input("두 개의 정수를 띄어쓰기로 구분하여 입력 >> ").split()
print(f"{data[0]} + {data[1]} = {int(data[0]) + int(data[1])}")
# %%
