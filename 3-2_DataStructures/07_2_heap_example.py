import heapq

numbers = [50, 20, 10, 80, 60, 30]
k = 3

heapq.heapify(numbers)

smallest = [heapq.heappop(numbers) for _ in range(k)]

print(smallest[-1])
