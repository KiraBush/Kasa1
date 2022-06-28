import library
import math
import numpy as np
import matplotlib.pyplot as plt


def getCentre(P):
    x = y = 0
    for point in P:
        x += point[0]
        y += point[1]
    lp = len(P)
    centre = [x / lp, y / lp]
    return centre


def read(filename):
    list1 = []
    list2 = []
    with open(filename) as f:
        for i in f.readlines():
            i = i.split()
            list1.append(i[0])
            list2.append(i[1])
    list1 = list(map(int, list1))
    list2 = list(map(int, list2))
    return list1, list2


library.input()
library.solve()

ansX, ansY = read('output.txt')
genX, genY = read('input.txt')

ans = list(zip(ansX, ansY))
centre = getCentre(ans)  # находим центр
ans.sort(key=lambda x: (math.atan2(x[1] - centre[1], x[0] - centre[0])))  # сортируем точки по часовой стрелке
ans.append(ans[0])

ansX, ansY = [x for x in zip(*ans)]
plt.plot(genX, genY, "ko")
plt.plot(ansX, ansY, "ro-")
plt.show()

# 25
# 81 41
# 163 243
# 34 248
# 79 233
# 233 121
# 62 153
# 80 164
# 64 108
# 37 49
# 175 134
# 235 183
# 246 159
# 160 49
# 229 155
# 98 28
# 216 167
# 231 194
# 230 62
# 178 111
# 210 175
# 221 12
# 131 241
# 117 206
# 178 119
# 191 114
