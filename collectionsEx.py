items = (
    ('A', 1),
    ('B', 2),
    ('C', 3),
)

def regular_dict_ex():
    print('====Regular Dict====')
    regular_dict = dict(items)
    for k, v in regular_dict.items():
        print (k, v)
regular_dict_ex()        

from collections import OrderedDict
def ordered_dict_ex():
    print('====Ordered Dict====')
    ordered_dict = OrderedDict(items)
    for k, v in ordered_dict.items():
        print (k, v)
ordered_dict_ex()

from collections import defaultdict
def def_defaultdict_ex():
    print("====default defaultdict====")
    state_capitals = defaultdict(lambda: 'Boston')
    state_capitals['Arkansas'] = 'Little Rock'
    state_capitals['California'] = 'Sacramento'
    print(state_capitals['Alabama']) #不存在的key返回預設值
def_defaultdict_ex()

def group_defaultdict_ex():
    print("====group defaultdict====")
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
group_defaultdict_ex()


"""
下面这个例子就是使用Counter模块统计一段句子里面所有字符出现次数
"""
from collections import Counter
def counter_ex():
    print("====counter 取得出现频率最高的5個字符====")
    s = '''A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.'''.lower()

    c = Counter(s)
    # 获取出现频率最高的5个字符
    print(c.most_common(5))
counter_ex()

#namedtuple
from collections import namedtuple
def namedtuple_ex():
    print("====namedtuple ex====")
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
namedtuple_ex()

# import os
# os._exit(0)

#deque
"""
下面这个是一个有趣的例子，主要使用了deque的rotate方法来实现了一个无限循环
的加载动画
"""
import sys
import time
from collections import deque

def deque_ex():
    fancy_loading = deque('>--------------------')

    tStart = time.time()

    while True:
        tEnd = time.time()

        if (tEnd - tStart) > 1:
            break    

        print ('\r%s' % ''.join(fancy_loading))
        fancy_loading.rotate(1)
        sys.stdout.flush()
        time.sleep(0.08)
deque_ex()

'''
window下，注释#sys.stdout.flush()代码行跟没有注释输出相同。
在linux下，注释#sys.stdout.flush()代码行时，是在间隔5秒后一下子输出1,2,3,4,5，而不注释是每间隔一秒输出一个数字
'''

'''
'%s %s' % ('one', 'two')   old
'{} {}'.format('one', 'two')  new
'''