#F(n) = F(n-1)+F(n-2)  where n>1
def fibo(n):
    if n==0:
        print(0)
    elif n==1:
        print(1)
    else:
        f1=0
        f2=1
        for i in range(n-1):
            f=f1+f2
            f1=f2
            f2=f
        print(f)
fibo(6)
