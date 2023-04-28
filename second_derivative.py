from fractions import Fraction
def getD(n):
    return [Fraction((i+1),i) for i in range (1, n)]
def getL(n):
    return [-Fraction((i),(i+1)) for i in range (1, n)]
def getU(funk, xStart=0, xEnd=1, h=0.25):
    return [funk(h*i) for i in range(round(xStart/h)+1, round(xEnd/h))] + [funk(xEnd)]
def getX(xStart=0, xEnd=1, h=0.25):
    return [h*i for i in range(round(xStart/h)+2, round(xEnd/h))] 
def getC(x, d, h):
    return [-Fraction((d[i]*x[i] - x[i+1]),(h**2)) for i in range(len(d))]
def LC(l,c):
    return  [round(l[i]*c[i]+c[i+1],2) for i in range(0, len(l)-1)]  
def secDer(funk, xStart=0, xEnd=1, h=0.25):
    xEnd = round(xEnd + h,3)
    xStart = round(xStart - 2*h,3)
    n = round((xEnd-xStart)/h)
    d = getD(n)
    l = getL(n)
    u = getU(funk, xStart, xEnd, h)    
    c = getC(u, d, h)
    return getX(xStart, xEnd, h), LC(l,c)


funk = lambda x: x**3
h = Fraction(1,4)
xStart, xEnd = -1,1

x_list, y_list = secDer(funk,xStart, xEnd, h)

print(*x_list, sep = "\t")
print(*y_list, sep = "\t")
