a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# TODO
i=2
while not a%i==0:
    if(a==1):
        break
    i+=1
if(i==a):
    print(str(a)+"は素数です")
else:
    print(str(a)+"は素数ではありません")


i=2
while not b%i==0:
    if(b==1):
        break
    i+=1
if(i==b):
    print(str(b)+"は素数です")
else:
    print(str(b)+"は素数ではありません")
