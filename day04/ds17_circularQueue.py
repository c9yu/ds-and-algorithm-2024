# date : 20240215
# file : ds17_circularQueue.py
# desc : 원형 큐 일반구현, 원형큐에서는 rear|front % SIZE의 개념이 중요

# 원형 큐의 경우 5자리를 전부 사용하지 않고 한 자리를 비운채 이를 계산에 사용


# Queue 풀 확인 함수
def isQueueFull():
    global SIZE, queue, front, rear
# 당길 필요 없으니 간단하게 처리된다.
    if (rear + 1) % SIZE == front:
        return True
    else:
        return False

# Queue 엠티 확인 함수
def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False
    
# Queue 데이터 삽입 함수
def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull() == True:
        print('큐가 꽉 찼습니다.')
        return
    else:
        rear = (rear+1) % SIZE # 원형 큐에서 데이터 입력 공간 확보 방법
        queue[rear] = data

# Queue 데이터 추출 함수
def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty() == True:
        print('큐가 비었습니다.')
        return
    else:
        front = (front+1) % SIZE
        data = queue[front]
        queue[front] = None
        return data

# 추출 데이터 확인 함수
def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty() == True:
        print('큐가 비었습니다.')
        return None
    else:
        return queue[(front + 1)% SIZE] #(front + 1) % SIZE != front + 1 % SIZE

# 전역변수
SIZE = 5 #int(input('큐 크기 입력(정수) > ')) # 상수(constant)
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__ == '__main__': # 메인 시작

    while True:
        select = input('삽입(e), 추출(d), 확인(p), 종료(x)')

        if select.lower() == 'e':
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
        elif select.lower() == 'x':
            break
        else:
            continue


