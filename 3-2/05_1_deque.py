from collections import deque

dq = deque(['A', 'B', 'C', 'D'])
print(dq)

dq.appendleft('AA')
dq.append('DD')
print(dq)

dq.popleft()
dq.popleft()
dq.pop()
dq.pop()
print(dq)