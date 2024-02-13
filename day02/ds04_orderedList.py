# date : 20240213
# file : ds03_orderedList.ipynb
# desc : 선형 리스트 프로그램

## 데이터 추가 함수

def add_data(friend):
    kakaotalk.append(None) # 배열에 빈 자리를 만든다.
    size = len(kakaotalk) # 배열 전체 크기를 확인
    kakaotalk[size - 1] = friend

## 데이터 삽입 함수

def insert_data(pos, friend):
    if pos < 0 or pos > len(kakaotalk):
        print('데이터 삽입범위 초과')
        return # 'return' 돌려주는 값이 없다 : 함수를 빠져나감
    
    # 정상적인 처리 시작
    kakaotalk.append(None) # 빈칸 추가
    size = len(kakaotalk) # 배열의 현재 크기

    # 데이터 삽입 위치까지 데이터를 하나씩 뒤로 보낸다.
    for i in range(size-1, pos, -1): # 뒤에서부터 하나씩 당겨주면서 빈자리를 만든다.
        kakaotalk[i] = kakaotalk[i - 1]
        kakaotalk[i - 1] = None # 이걸 pos(목표 위치)까지 반복
    
    kakaotalk[pos] = friend

## 데이터 삭제 함수
    
def delete_data(pos): # 데이터 삭제시는 위치값만 들어간다.
    if pos < 0 or pos >= len(kakaotalk): # 교재 103p 에는 >가 되어 있으나, >=가 맞다.
        print('데이터 삭제범위 초과')
        return
    
    size = len(kakaotalk)
    kakaotalk[pos] = None # 데이터 삭제

    for i in range(pos+1, size): # range(pos+1, size, 1) 과 같은 내용
        kakaotalk[i-1] = kakaotalk[i] # 뒤의 값을 앞으로 
        kakaotalk[i] = None

    del(kakaotalk[size-1]) # 배열의 맨 마지막 값 삭제

kakaotalk = [] # 빈 배열생성
select = -1

if __name__ == '__main__':
    while (select != 4):
        select = int(input('선택(1:추가. 2:삽입, 3:삭제, 4:종료) > '))

        if select == 1:
            data = input('추가 데이터 --> ')
            add_data(data)
            print(kakaotalk)

        elif select == 2:
            pos = int(input('삽입위치 --> '))
            data = input('추가 데이터--> ')
            insert_data(pos, data)
            print(kakaotalk)

        elif select == 3:
            pos = int(input('삭제위치 --> '))
            delete_data(pos)
            print(kakaotalk)

        elif select == 4:
            exit(0) # exit는 break문과 다르게 프로그램을 완전 종료하는 함수

        else:
            print('1~4 중 하나를 입력하세요')
            continue