import time
import sys
for i in range(10):
    sys.stdout.write("\r{0}>".format("="*i))
    sys.stdout.flush()
    time.sleep(0.5)

'''
window下，注释#sys.stdout.flush()代码行跟没有注释输出相同。
在linux下，注释#sys.stdout.flush()代码行时，是在间隔5秒后一下子输出1,2,3,4,5，而不注释是每间隔一秒输出一个数字
'''    