print(all(['a','b','c','d']))# 列表list，元素都不为空或0  True
print(all(['a','b','','d']))# 列表list，存在一个为空的元素 False
print(all([-1,1,2,3])) # 列表list，元素都不为空或0  True
print(all([0,1,2,3]))# 列表list，存在一个为0的元素 True
print(all([])) # 空列表 False

data = ['a','b','c','d']
checks = ['a','b1']
res = map(lambda x:x in data,checks)
print(res)
print(all(res))
#用()也一樣