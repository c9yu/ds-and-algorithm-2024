# date : 20240213
# file : ds07_simpleLinkedList.py
# desc : 단순 연결 리스트 일반 구현

memory = [] # memory라는 이름의 빈 리스트 생성, 컴퓨터 메모리를 유사하게 구성
# head, curr, prev 일반 변수
head, curr, prev = None, None, None

class Node():
    def __init__(self, name) -> None:
        self.data = name
        self.link = None

# 클래스 끝
def printNodes(start): # printNodes(self, start) 가 아니다 즉, self가 아니므로 class에 포함되지 않고(멤버 함수가 X), 들여쓰기 하지 않는다.
    curr= start
    if curr == None : return # 다음 값이 없으니까 함수를 빠져나감
    print(curr.data, end = ' -> ')
    while curr.link != None:
        curr = curr.link # 내 노드 다음의 노드가 current가 됨
        print(curr.data, end = ' -> ') # end -> 로 해서 enter가 없음
    print() # enter 추가

dataArray = ['다현', '정연', '쯔위', '사나', '지효']

if __name__ == '__main__':
    node = Node(dataArray[0])
    head = node # 첫번째 값을 head가 가리킴
    memory.append(node)

    for data in dataArray[1:]: # 두 번째 노드부터 끝까지
        prev = node
        node = Node(data) # 정연
        prev.link = node
        memory.append(node)

    printNodes(head)