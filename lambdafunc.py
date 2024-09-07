""" lambda function is called as anonymus function. It is written in one line """
a,b=map(int,input("enter first no.s").split())
x=lambda  a,b: a+b
print(x(a,b))