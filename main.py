# Python 3
from fractions import Fraction
import string
import math
N = 25 # 丟幾次硬幣?

trying = int(math.pow(2, N)) # 所有的組合數
list1 = [] # 儲存所有可能的組合

# 找出所有組合
for i in range(0,trying):
    listTemp = []
    binary = format(i, "b").zfill(N)
    for x in binary:
        listTemp.append(x)
    list1.append(listTemp)

list1.pop(0) # 刪除都是0的組合
list1.pop(0) # 刪除只有尾巴是1其他都是0的組合

# 可進行計算的整數
#print(list1)

tot = 0
half = 0
for l in list1:
    child = 0 # 分子
    parent = 0 # 分母
    for idx,val in enumerate(l):
        if idx > 0 and l[idx-1] == '1':
            parent+=1
        if idx + 1 < len(l) and l[idx] == '1' and l[idx+1] == '1':
            child+=1

    tot += Fraction(child,parent)
    if child/parent == 0.5:
        half+=1

print("Q1:",Fraction(tot,len(list1)))
print("Q2:",half)