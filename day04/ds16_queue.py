# date : 20240215
# file : ds16_queue.py
# desc : 큐 일반 구현

# Queue 풀 확인 함수
def isQueueFull():
    global SIZE, rear
    if rear == (SIZE - 1):
        return True
    else:
        return False
    
# Queue 엠티 확인 함수
def isQueueEmpty():
    global SIZE, rear
    if front == rear:
        return True
    else:
        return False
    
# Queue 데이터 삽입 함수
def enQueue(data):
    global queue, rear
    if isQueueFull() == True:
        print('큐가 꽉 찼습니다.')
        return
    else:
        rear += 1
        queue[rear] = data

# Queue 데이터 추출 함수
def deQueue():
    global queue, front
    if isQueueEmpty() == True:
        print('큐가 비었습니다.')
        return
    else:
        front += 1
        data = queue[front]
        queue[front] = None
        return data

# 추출 데이터 확인 함수
def peek():
    global queue, front
    if isQueueEmpty() == True:
        print('큐가 비었습니다.')
        return None
    else:
        return queue[front + 1]

# 전역변수
SIZE = int(input('큐 크기 입력(정수) > ')) # 상수(constant)
queue = [None for _ in range(SIZE)]
front = rear = -1

if __name__ == '__main__': # 메인 시작
    while True:
        select = input('삽입(e), 추출(d), 확인(p), 종료(x)')

        if select.lower():
            data = input('입력 데이터 > ')
            enQueue(data)
            print(f'큐상태 : {queue}')
        elif select.lower() == 'd':
            data = deQueue()
            print(f'추출 데이터 > {data}')
            print(f'큐 상태 > {queue}')
        elif select.lower() == 'p':
            data = peek()
            print(f'확인 데이터 > {data}')
            print(f'큐 상태 > {queue}')
            break
        else:
            continue


    # front = rear = -1

    # print(queue)
    # enQueue('선미')
    # print(queue)
    # enQueue('재남')

    # queue = ['화사', None, None, None, None]
    # front = -1
    # rear = 0

    # print(queue)
    # print(deQueue())
    # print(queue)
    # print(deQueue())
