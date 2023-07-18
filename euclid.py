a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
import random

#最大公約数を求める関数
def euclid(a, b):
    r=a%b
    while not r==0:
        a=b
        b=r
        r=a%b
    return b

#互いに素かどうか判定する関数
def euclid2(a, b):
    answer=euclid(a, b)
    if answer==1:
        return True
    else:
        return False

answer=euclid(a, b)
answer2=euclid2(a, b)
print("最大公約数は"+str(answer)+"です")
if(answer2):
    print("互いに素です")
else:
    print("互いに素ではありません")


#エクストラ問題
A=0
for i in range(100000):
    x=random.randint(1, 10000)
    y=random.randint(1, 10000)
    z=euclid2(x, y)
    if(z):
        A+=1
print("エクストラ問題の解は"+str(A/100000)+"です")
