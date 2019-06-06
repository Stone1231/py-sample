# 一般來說，物件導向語言中的「class」是用來「描述如何建立 object」的程式碼；
# 我們寫 class 就是為了建立 object。
# 然而在 Python 中：
# 連 class 本身也是 object
# class 是 metaclass 的 instance。
# metaclass 是 class 的 class。

# 當寫下 class 關鍵字 ，Python 會執行它，並建立一個 class object
# 這個 class object 並不是 class instance，而是 class 自己本身。
# 這個 class object 的功能就是建立自己的 instance object。

# type 是 Python 中的 metaclass:
# type 本身也是一個 class
# type 本身的 metaclass 就是他自己
# 要寫一個 metaclass 的話，就繼承 type
#__call__() 預設會呼叫 __new__() 跟 __init__()
# Hello() , Hello.__call__() 一樣


class Hello:   # 預設繼承自 object
    pass

print( Hello         )         # <class '__main__.Hello'>
print( Hello()       )         # <__main__.Hello object at 0x7f1cc5aedcc0>
print( type(Hello)   )         # <class 'type'>
print( type(Hello()) )         # <class '__main__.Hello'>

# 手動寫法
DynamicHello = type("DynamicHello", (), {})

print( DynamicHello         )  # <class '__main__.DynamicHello'>
print( DynamicHello()       )  # <__main__.DynamicHello object at 0x7f1cc5aedcc0>
print( type(DynamicHello)   )  # <class 'type'>
print( type(DynamicHello()) )  # <class '__main__.DynamicHello'>

title = "The C++ Programming Language"
page = 42
def func():
    pass
hello = Hello()    

print(func.__class__)   # <class 'function'>
print(title.__class__)  # <class 'str'>
print(page.__class__)   # <class 'int'>
print(hello.__class__)  # <class '__main__.Hello'>

#Python 裡面所有的 class 都是 type 的 instance
print(title.__class__.__class__)  # <class 'type'>
print(page.__class__.__class__)   # <class 'type'>
print(func.__class__.__class__)   # <class 'type'>
print(hello.__class__.__class__)  # <class 'type'>
    