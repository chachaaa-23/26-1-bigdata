import sys
import array

list_ = [i for i in range(100000)]
array_ = array.array('i', list_)

lust_ = [i for i in range(100000)]

list_ = []
for i in range (100000):
    list.append(i)

print(f"List size: {sys.getsizeof(list_)} bytes")
print(f"Array size: {sys.getsizeof(array_)} bytes")