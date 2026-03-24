from collections import deque
# 앞, 뒤에서 넣고 빼기 모두 가능
#stack+ queue 합친버전

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