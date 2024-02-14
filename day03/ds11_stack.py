# date : 20240214
# file : ds11_stack.ipynb
# desc : 스택 전체 구현

# 스택 Full 확인 함수
def isStackFull():
    global SIZE, stack, top
    if top == (SIZE-1):
        return True # 스택이 꽉 찼음
    else:
        return False

# 스택 push 함수
def push(data):
    global SIZE, stack, top
    if isStackFull() == True: # 데이터를 넣을 수 없다.
        print('스택이 꽉 찼습니다.')
        return
    else:
        top += 1
        stack[top] = data

# 스택 Empty 확인 함수
def isStackEmpty():
    global SIZE, stack, top
    if top <= -1 :
        return True # 스택이 비었음
    else:
        return False
    
# 스택 pop 함수
def pop():
    global SIZE, stack, top
    if isStackEmpty() == True:
        print('스택이 비었습니다.')
        return None
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
    
# 스택 최종 데이터 확인 함수
def peek():
    global stack, top
    if isStackEmpty() == True:
        print('스택이 비었습니다.')
        return None
    else:
        return stack[top]
    
# 전역 변수 선언
SIZE = 5 # 5칸짜리 스택
stack = [None for _ in range(SIZE)]
top = -1

# 메인 코드
if __name__ == '__main__':

    while True:
        select = input('PUSH(p),POP(o),PEEK(e),Exit(x)')

        if select.lower() == 'p':
            data = input('입력데이터>> ')
            push(data)
            print(f'스택상태 : {stack}')
        elif select.lower()=='o':
            data = pop()
            print(f'추출 데이터 : {data}')
            print(f'스택상태 : {stack}')
        elif select.lower() == 'e':
            data = peek()
            print(f'확인 데이터 : {data}')
            print(f'스택상태 : {stack}')
        elif select.lower() == 'x':
            exit(0)
        else:
            continue