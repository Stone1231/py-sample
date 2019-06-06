class Foo(object):
    foo = 'attr foo of Foo'
    def get_str(self):
        return "hello~"

class Bar(object):
    foo = 'attr foo of Bar' # we won't see this.
    bar = 'attr bar of Bar'
    def get_str(self):
        return "hi~"
    def output(self):
       s = self.get_str() # 會call Foo
       print(f"{s} {self.foo}")

class FooBar(Foo, Bar):# 前面優先
    foobar = 'attr foobar of FooBar'

fb = FooBar()    
fb.output()