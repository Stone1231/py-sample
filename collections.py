#OrderedDict
from collections import OrderedDict

items = (
    ('A', 1),
    ('B', 2),
    ('C', 3),
)

regular_dict = dict(items)
ordered_dict = OrderedDict(items)

print('Regular Dict:')
for k, v in regular_dict.items():
    print (k, v)

print('Ordered Dict:')
for k, v in ordered_dict.items():
    print (k, v)

#defaultdict
from collections import defaultdict

members = [
    # Age, name
    ['male', 'John'],
    ['male', 'Jack'],
    ['female', 'Lily'],
    ['male', 'Pony'],
    ['female', 'Lucy'],
]

result = defaultdict(list)
for sex, name in members:
    result[sex].append(name)

print (result)

#Counter
"""
下面这个例子就是使用Counter模块统计一段句子里面所有字符出现次数
"""
from collections import Counter

s = '''A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.'''.lower()

c = Counter(s)
# 获取出现频率最高的5个字符
print(c.most_common(5))


#namedtuple
from collections import namedtuple

websites = [
    ('Sohu', 'http://www.google.com/', u'张朝阳'),
    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
    ('163', 'http://www.163.com/', u'丁磊')
]

Website = namedtuple('Website', ['name', 'url', 'founder'])

for website in websites:
    print (website)
    website = Website._make(website)
    print (website)

#deque
"""
下面这个是一个有趣的例子，主要使用了deque的rotate方法来实现了一个无限循环
的加载动画
"""
import sys
import time
from collections import deque

fancy_loading = deque('>--------------------')

while True:
    print ('\r%s' % ''.join(fancy_loading))
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)


'''
window下，注释#sys.stdout.flush()代码行跟没有注释输出相同。
在linux下，注释#sys.stdout.flush()代码行时，是在间隔5秒后一下子输出1,2,3,4,5，而不注释是每间隔一秒输出一个数字
'''

'''
'%s %s' % ('one', 'two')   old
'{} {}'.format('one', 'two')  new
'''