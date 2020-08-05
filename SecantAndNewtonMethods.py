''' Writing python codes of Newton and Secant methods. It combines them with an if loop and gives the 
solution with the newton method when the user enters 1, and the secant method with 2 entries.'''
from math import cos,sin

def f(x):
    return x*x*x+sin(x)

def f1(x):
    return 3*(x*x)+cos(x)

def newton():
    a0=6
    for i in range(0,5):
        a1=a0-(f(a0)/f1(a0))
        hata=abs(a1-a0)
        a0=a1
        print("value of the root= ",a1, "tolerance= ",hata)
    return None

def secant():
    a=3
    b=6
    for i in range(6):
        bn=b-((f(b)*(b-a))/(f(b)-f(a)))
        a=b
        b=bn
        print(b)
    return None

#x(i+1)=bn x(i)=bx(i-1)=a

sec=input('Enter 1 for the newton method and 2 for the secant method.')
if sec=='1':
    print("newton method results:")
    newton()
if sec=='2':
    print("secant method results:")
    secant()