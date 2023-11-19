import random

"""선택정렬"""
def selection_sort(numList): # 선택정렬 실행
    print("<선택정렬>")
    print("정렬 전 : ", numList) #정렬 전 리스트 출력

    n = len(numList) # 정렬의 길이 저장(numList의 길이)

    for i in range(n-1) : # 정렬의 길이 만큼 반복
        least = i #현재 인덱스를 최소값으로 설정

        for j in range(i+1, n): # 최소값 탐색
            if numList[j] < numList[least]: # 현재 인덱스의 값보다 작은 값을 찾으면
                least = j # 최소값 갱신

        numList[i], numList[least] = numList[least], numList[i] # 현재 인덱스와 최소값의 위치 교환

    print("정렬 후 : ", numList) #정렬 후 리스트 출력

"""삽입정렬"""
def insertion_sort(numList): # 삽입정렬 시작
    print("<삽입정렬>")
    print("정렬 전 : ", numList) # 정렬 전 리스트 출력

    n = len(numList) # 정렬의 길이 저장(numList의 길이)

    for i in range(n-1): # 정렬 길이 만큼 반복
        key = numList[i] # 지금 위치를 key로 선택
        j = i-1 # 지금 이전의 위치를 j로 설정

        while j >= 0 and numList[j] > key: #key보다 큰 값을 찾으면 이동
            numList[j+1] = numList[j] # 현재 값보다 큰 값을 오른쪽으로 이동
            j -= 1

        numList[j+1] = key # 다음값을 key로 설정

    print("정렬 후 : ", numList) # 정렬 후 리스트 출력

"""버블정렬"""
def bubble_sort(numList): # 버블 정렬 시작
    print("<버블정렬>")
    print("정렬 전 : ", numList)  # 정렬 전 리스트 출력

    n = len(numList) # 리스트의 길이 저장 (numList의 길이)

    for i in range(n - 1, 0, -1):  # 리스트의 마지막 요소부터 첫 번째 요소까지 역순으로 반복

        for j in range(i):  # 첫 번째 요소부터 마지막에서 i번째 요소까지 반복

            if numList[j] > numList[j + 1]:  # 현재 요소가 다음 요소보다 크면 두 요소를 교환
                numList[j], numList[j + 1] = numList[j + 1], numList[j]

    print("정렬 후 : ", numList) # 정렬 후 리스트 출력

"""퀵 정렬"""
def quick_sort(numList, left, right): #퀵정렬 시작
    # numList: 정렬할 숫자들이 담긴 리스트
    # left: 현재 정렬 범위의 왼쪽 인덱스
    # right: 현재 정렬 범위의 오른쪽 인덱스

    if left < right:
        i = left + 1 #i는 왼쪽에서 1더한 위치
        j = right # j는 젤 오른쪽 값
        pivot = numList[left] # 피벗은 현재 범위의 가장 왼쪽 값으로 선택

        while i <= j: #i가 오른쪽까지 왔거나 작을때

                while i <= right and numList[i] <= pivot: # 피벗보다 작은 값을 찾을 때까지
                    i += 1 #오른쪽으로 이동

                while j >= left and numList[j] > pivot: # 피벗보다 큰 값을 찾을 때까지
                    j -= 1 #왼쪽으로 이동

                if i < j: #i가 j보다 작으면
                    numList[i], numList[j] = numList[j], numList[i] # 두 값 교환

        numList[left], numList[j] = numList[j], numList[left] # 피벗 위치 조정

        quick_sort(numList, left, j - 1) # 피벗을 기준으로 왼쪽과 오른쪽 부분에 대해 재귀적으로 퀵 정렬 수행
        quick_sort(numList, j + 1, right)

# sorted = [0 for _ in range(25)]  # 합병정렬시 사용

sorted = [0] * 25

"""합병 정렬"""
def merge(numList, left, mid, right):
    # A: 정렬될 리스트
    # left: 왼쪽 리스트의 시작 인덱스
    # mid: 중간 지점 인덱스
    # right: 오른쪽 리스트의 끝 인덱스

    global sorted
    i = left # 왼쪽 리스트의 첫 번째 인덱스
    j = mid + 1 # 오른쪽 리스트의 첫 번째 인덱스
    k = left # 정렬될 리스트의 첫 번째 인덱스

    # 왼쪽과 오른쪽 리스트를 비교하여 작은 값을 sorted 리스트에 저장
    while i <= mid and j <= right:
        if numList[i] <= numList[j]:
            sorted[k] = numList[i] # 왼쪽 리스트의 현재 값이 작거나 같으면 sorted 리스트에 추가
            i, k = i + 1, k + 1 #  왼쪽 리스트와 sorted 리스트의 인덱스를 증가
        else:
            sorted[k] = numList[j] # 오른쪽 리스트의 현재 값이 작으면 sorted 리스트에 추가
            j, k = j + 1, k + 1 # 오른쪽 리스트와 sorted 리스트의 인덱스를 증가

    # 남아있는 리스트의 값들을 복사
    if i > mid:
        # 왼쪽 리스트의 값이 모두 사용된 경우
        sorted[k : k + right - j + 1] = numList[j : right + 1]
    else :
        # 오른쪽 리스트의 값이 모두 사용된 경우
        sorted[k : k + mid - i + 1] = numList[i : mid + 1]

    # 임시(sorted[]) 리스트를 원래(A[]) 리스트로 복사
    numList[left : right + 1] = sorted[left : right + 1]

"""합병 정렬"""
def merge_sort(numList, left, right):
    if left < right:
        mid = (left + right) // 2  # 현재 리스트를 두 개의 작은 리스트로 나누는 중간 지점 계산
        merge_sort(numList, left, mid)  # 왼쪽 부분 리스트에 대해 재귀적으로 병합 정렬 수행
        merge_sort(numList, mid + 1, right)  # 오른쪽 부분 리스트에 대해 재귀적으로 병합 정렬 수행
        merge(numList, left, mid, right)  # 두 개의 작은 정렬된 리스트를 합병하여 정렬된 리스트로 만듦

"""힙 정렬 1"""
def heapPush(numList1, n):
    # 힙에 원소를 추가하고 힙 속성을 유지
    numList1.append(n) # 리스트에 값 추가
    i = len(numList1) - 1 # 추가된 값의 인덱스를 가져오기

    # 추가된 값이 부모보다 크면서 루트에 도달하지 않을 때까지 반복
    while i != 0 and n > numList1[i // 2]:
        numList1[i] = numList1[i // 2 ] # 부모 값을 현재 위치로 이동
        i //= 2 # 부모 노드로 이동
    numList1[i] = n # 마지막으로 삽입한 위치에 값을 삽입

"""힙 정렬 1"""
def heapPop(numList1): #힙에서 최댓값을 제거하고 반환
    size = len(numList1) - 1 # 힙에서 최댓값을 제거하고 반환

    if size == 0:
        return None # 힙이 비어있으면 None 반환

    p = 0 # 부모 노드의 인덱스
    i = 1 # 왼쪽 자식 노드의 인덱스
    root = numList1[0] # 힙의 루트 값 (최댓값)
    last = numList1[size] # 힙의 마지막 값

    while i <= size:
        if i < size and numList1[i] < numList1[i + 1]: # 두 자식 중 큰 값을 찾기
            i += 1 # 다음값으로 변경
        if last >= numList1[i]:  # 마지막 값이 현재 자식 값보다 크거나 같으면 루프 종료
            break #중지
        numList1[p] = numList1[i] # 현재 자식 값을 부모로 이동
        p = i # 현재 자식 노드의 인덱스를 부모로 설정
        i *= 2 # 다음 레벨의 왼쪽 자식 노드의 인덱스로 이동

    numList1[p] = last # 마지막 값이 적절한 위치로 이동
    numList1.pop() # 힙에서 마지막 값 제거
    return root # 최댓값 반환

"""힙 정렬 1"""
def heap_sort(numList1): #리스트를 힙에 넣고 다시 꺼내어 정렬
    heap = [0] # 힙 초기화

    for e in numList1: #길이만큼 반복
        heapPush(heap, e) # 리스트를 힙에 넣기

    for i in range(1, len(numList1) + 1): # 힙에서 값을 꺼내어 정렬된 리스트로 만들기
        numList1[-i] = heapPop(heap) # 힙에서 최대값(루트)을 제거하고 정렬된 순서로 리스트에 저장

    return numList1 # 정렬된 리스트 반환

"""힙 정렬 2"""
def heapify(numList2, n, i):
    # 현재 노드를 가장 큰 값으로 설정
    largest = i
    # 왼쪽 자식 노드의 인덱스 계산
    l = 2 * i
    # 오른쪽 자식 노드의 인덱스 계산
    r = 2 * i + 1

    # 왼쪽 자식이 힙의 크기 내에 있고, 현재 값보다 크면
    if l <= n and numList2[i - 1] < numList2[l - 1]:
        largest = l # largest를 왼쪽으로 이동
    # 오른쪽 자식이 힙의 크기 내에 있고, 현재 값보다 크면
    if r <= n and numList2[largest - 1] < numList2[r - 1]:
        largest = r #largest를 오른쪽 자식으로 이동

    # largest가 변경되었다면 하고
    if largest != i:
        numList2[i - 1], numList2[largest - 1] = numList2[largest - 1], numList2[i - 1] #현재 노드와 largest 노드의 값을 교환
        heapify(numList2, n, largest) # heapify 호출

"""힙 정렬 2"""
def heapSort(numList2):
    n = len(numList2) - 1 # 리스트의 크기

    # 최대 힙 구하기
    # 리스트의 중간부터 시작하여 루트까지 거꾸로 탐색하며 각 노드에 대해 heapify 함수를 호출하여 최대 힙을 만듦
    for i in range(n // 2, 0, -1):
        heapify(numList2, n, i)

    # 최대 힙 조건을 만족하도록 각 노드를 조정.
    for i in range(n // 2, 0, -1):
        heapify(numList2, n, i)

    # 힙에서 원소 하나씩 꺼내어 정렬
    for i in range(n - 1, 0, -1):
        numList2[i], numList2[0] = numList2[0], numList2[i] # 최대값을 마지막 값과 교환
        heapify(numList2, i, 1) # 교환된 후에도 최대 힙을 유지하기 위해 heapify 호출
    return numList2 # 정렬된 리스트 반환

""" main """
def main():
    print("*****************************")
    print("*** 여러가지 정렬 프로그램 구현 ***")
    print("***                       ***")
    print("*** 1. 선택(selection) 정렬 ***")
    print("*** 2. 삽입(insertion) 정렬 ***")
    print("*** 3. 버블(bubble) 정렬    ***")
    print("*** 4. 퀵(quick) 정렬      ***")
    print("*** 5. 합병(merge) 정렬     ***")
    print("*** 6. 힙(heap) 정렬       ***")
    print("*** 7. 종료(quit)         ***")
    print("*****************************")

    while True:
        """랜덤 변수"""
        numList = list()
        while True:
            if len(numList) == 25:
                break
            num = random.randrange(0, 101)
            numList.append(num)

        num = int(input("번호 입력 : "))

        if (num == 7):
            print("<종료>")
            break

        elif (num == 1):
            selection_sort(numList)

        elif (num == 2):
            insertion_sort(numList)

        elif (num == 3):
            bubble_sort(numList)

        elif (num == 4):
            print("<퀵 정렬>")
            print("정렬 전 : ", numList)  # 정렬 전 리스트 출력
            quick_sort(numList, 0, len(numList) - 1)
            print("정렬 후 : ", numList) #정렬 후 리스트 출력

        elif (num == 5):
            print("<합병 정렬>")
            print("정렬 전 : ", numList)  # 정렬 전 리스트 출력
            merge_sort(numList, 0, len(numList) - 1)
            print("정렬 후 : ", numList)

        elif (num == 6):
            numList1 = list(numList)
            numList2 = list(numList)
            print("<힙 정렬1>")
            print("정렬 전 : ", numList1)  # 정렬 전 리스트 출력
            heap_sort(numList)
            print("정렬 후 :", numList) #정렬 후 리스트 출력

            print("<힙 정렬2>")
            print("정렬 전 : ", numList2)  # 정렬 전 리스트 출력
            heapSort(numList)
            print("정렬 후 : ", numList) #정렬 후 리스트 출력

        else:
            print("<번호 오류>")

if __name__ == "__main__":
    main()
