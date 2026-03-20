from collections import deque

dq = deque([])
print(dq)

dq.append('Daniel')
dq.appendleft('James')
dq.appendleft('Benjamin')
dq.append('Sophia')
dq.appendleft('Olivia')
dq.appendleft('Grace')
dq.append('Potter')
dq.append('William')
print(dq)

dq.popleft()
dq.popleft()
dq.pop()
print(dq)