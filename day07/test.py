import random
## 함수 선언 부분##
class TreeNode():
    def __init__(self) -> None:
        self.left = None
        self.data = None
        self.right = None


# 전역 변수 선언 부분
memory = []
root = None
dataAry = []
# dataAry.append(input())
# dataAry.append(input())
# dataAry.append(input())
# dataAry.append(input())
# dataAry.append(input())
# dataAry.append(input())
# dataAry.append(input())
while True:
        select = input('물건 추가(e), 물건 제거(d), 종료(x)')

        if select.lower() == 'e':
            dataAry.append(input('물건 추가 -> '))
            enQueue(dataAry)
            print(f'현재 물건 상태 : {dataAry}')
            
        elif select.lower() == 'd':
            dataAry = deQueue()
            print(f'물건 제거 > {dataAry}')
            print(f'현재 물건 상태 > {dataAry}')

        elif select.lower() == 'p':
            dataAry = peek()
            print(f'확인 데이터 > {dataAry}')
            print(f'현재 물건 상태 > {dataAry}')
        elif select.lower() == 'x':
            break
        else:
            continue

sellAry = [random.choice(dataAry) for _ in range(20)]

print('오늘 판매된 물건(중복0) --> ', sellAry)

## 메인 코드 부분 ##
node = TreeNode()
node.data = sellAry[0]
root = node
memory.append(node)

for name in sellAry[1:] :

    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name == current.data:
            break
        if name < current.data:
            if current.left == None:
                current.left = node
                memory.append(node)
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                memory.append(node)
                break
            current = current.right

print('이진 탐색 트리 구성 완료!')

def preorder(node):
    if node == None:
        return
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)

print('오늘 판매된 종류(중복X) --> ', end=' ')
preorder(root)