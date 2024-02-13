# date : 20240213
# file : ds05_orderedList.piynb
# desc : 선형 리스트 표현과 계산 프로그램

def printPoly(p_x):
    term = len(p_x)-1
    polyStr = "P(x) = "

    for i in range(len(px)):
        coef = p_x[i]

        if (coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + ""
        term -= 1
    
    return polyStr

def calcPoly(xVal, p_x):
    retValue = 0
    term = len(p_x)-1

    for i in range(len(px)):
        coef = p_x[i]
        retValue += coef*xVal**term
        term -= 1

    return retValue

## 전역변수

px = [7, -4, 0, 5]

if __name__ == "__main__":
    pStr = printPoly(px)
    print(pStr)

    xValue = int(input("X 값 --> "))
    
    pxValue = calcPoly(xValue, px)
    print(pxValue)

################################
    
##함수 선언 부분 ##
def printPoly (t_x, p_x) :
    polyStr = "P(x) = "

    for i in range (len (p_x)) :
        term = t_x[i] # 항 차수
        coef = px[i] # 계수

        if (coef >= 0) :
            polyStr += ""
        polyStr += str(coef) + "x^" + str(term) + " "

    return polyStr


def calcPoly(xVal, t_x, p_x) :
    retValue = 0

    for i in range(len (px)) :
        term = t_x[i] # 항 차수
        coef = p_[i] # 계수
        retValue += coef * xValue ** term


    return retValue