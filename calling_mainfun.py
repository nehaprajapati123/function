def fun1(a,b):
    c=(a+b)
    return c
def fun2(x,y):
    d=(x-y)
    return d
def fun3(m,n):
    e=(m*n)
    return e
def fun4(o,p):
    f=(o/p)
    return f
def main():
    if sign=="+":
        print (fun1(3,7))
    elif sign=="-":
        print (fun2(10,7))
    elif sign=="*":
        print (fun3(6,9))
    elif sign=="/":
        print (fun4(2,6))
sign=input('enter your sign:-')
main()