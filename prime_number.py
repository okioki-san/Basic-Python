n = float(input("nの値を入力: "))

# TODO
def prime_number(n):
    if(n<=1 or n%1!=0):
        return False
    i=2
    while not n%i==0:
        i+=1
    if(i==n):
        return True
    else:
        return False
    
result=prime_number(n)
if result:
    print(str(n)+"は素数です")
else:
    print(str(n)+"は素数ではありません")