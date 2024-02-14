# date : 20240214
# file : ds13_stack.ipynb
# desc : 스택 전체 구현

import webbrowser
import time

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
SIZE = 10 # 10칸짜리 스택
stack = [None for _ in range(SIZE)]
top = -1

# 메인 코드
if __name__ == '__main__':
    urls = ['naver.com','daum.net','nate.com','bing.com','github.com']

    for url in urls:
        push(url)
        webbrowser.open(f'https://www.{url}')
        print(url, end = ' --> ')
        time.sleep(1) # 잠시 초 단위로 재운다(멈춘다). : time.sleep(1): 1초 멈춘 뒤 진행.

    print('방문 종료')
    time.sleep(5) # 5초동안 멈춘다.
    
    print(stack)

    while True:
        url = pop()
        if url == None: break

        webbrowser.open(f'https://www.{url}')
        print(url, end=' --> ')
        time.sleep(1)

    print('방문 종료')