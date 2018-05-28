class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

e1 = Node('Mon')
e2 = Node('Wed')
e3 = Node('Tue')
e4 = Node('Thu')

e1.nextval = e3
e3.nextval = e2
e2.nextval = e4

thisvalue = e1

while thisvalue:
    print(thisvalue.dataval)
    thisvalue = thisvalue.nextval