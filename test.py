import collections
import random

#a = [1,2,3,2,1,5,6,5,5,5]

#print([item for item, count in collections.Counter(a).items() if count >= 1])

#b = [(item,count) for item, count in collections.Counter(a).items() if count >= 1]
#a = [(1, 2), (3, 2), (4, 2), (5, 3), (6, 2), (7, 2), (8, 3), (9, 2), (10, 2), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 2), (18, 2), (19, 3), (20, 3), (21, 3), (22, 2), (23, 3), (24, 3), (25, 3), (26, 3), (27, 3)]
#a.reverse()
#print(a)

test = "ab12.4"
test = "".join(i for i in test if i.isdigit() or i == ".")
print(test)