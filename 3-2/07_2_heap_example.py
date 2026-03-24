import heapq
#min heap 라이브러리

numbers = [50, 20, 10, 80, 60, 30]
k = 3

heapq.heapify(numbers)

# min heap 의 요소들 pop, 오름차순 list 생성
smallest = [heapq.heappop(numbers) for _ in range(k)]

print(smallest[-1])
