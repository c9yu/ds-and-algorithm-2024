# date 20240219
# file : ds23_rcSum.py
# desc 재귀 호출 합산 함수

def addNumber(num):
    if num <= 1:
        return 1
    
    return num + addNumber(num-1) # 5 + addNumber(4)[4 + addNumber(3)[3 + addNuber(2)[2 + addNumber(1)]]]

sum = addNumber(5) # 15
print(sum)

for i in range(1,6):
    print(sum)