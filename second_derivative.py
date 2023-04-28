import math


def getD(n):
    return [(i+1)/i for i in range (1, n)]
def getL(n):
    return [-(i)/(i+1) for i in range (1, n)]
def getX(funk, xStart=0, xEnd=1, h=0.25):
    return [funk(h*i) for i in range(round(xStart/h)+1, round(xEnd/h))] + [funk(xEnd)]
def getC(x, d, h):
    return [-round((d[i]*x[i] - x[i+1])/(h**2),3) for i in range(len(d))]
def LC(l,c):
    return  [round(l[i]*c[i]+c[i+1],2) for i in range(0, len(l)-1)]  
def secDer(funk, xStart=0, xEnd=1, h=0.25):
    xEnd = round(xEnd + h,3)
    xStart = round(xStart - 2*h,3)
    n = round((xEnd-xStart)/h)
    d = getD(n)
    l = getL(n)
    u = getX(funk, xStart, xEnd, h)    
    c = getC(u, d, h)
    return LC(l,c)


funk = lambda x: x**3
h = 0.25
xStart, xEnd = map(int,input("Введіть [x0,xn]:  ").translate({ord(i): None for i in '[ ]'}).split(","))

print(secDer(funk,xStart, xEnd, h))

