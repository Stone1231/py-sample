#all 一個以上有值就是True
print(all(['a','b','c','d']))# 列表list，元素都不为空或0  True
print(all(['a','b','','d']))# 列表list，存在一个为空的元素 False
print(all([-1,1,2,3])) # 列表list，元素都不为空或0  True
print(all([0,1,2,3]))# 列表list，存在一个为0的元素 False
print(all([0,0,0,0]))# False
print(all([False,False]))# False
print(all([])) # 空列表 True

data = ['a','b','c','d']
checks = ['a','b1']
res = list(map(lambda x:x in data,checks)) #用set也可, 這邊map是方法,跟java的map不一樣
print(res)
print(all(res))

#any 一個以上有值就是True
print(any(['a','b','c','d']))# 列表list，元素都不为空或0  True
print(any(['a','b','','d']))# 列表list，存在一个为空的元素 True
print(any([-1,1,2,3])) # 列表list，元素都不为空或0  True
print(any([0,1,2,3]))# 列表list，存在一个为0的元素 True
print(any([0,0,0,0]))# False
print(any([False,False]))# False
print(any([])) # 空列表 False
print(any(res))