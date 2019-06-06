class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    # Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next=NewNode

    # Function to add node
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode
		
    # Function to remove node
    def RemoveNode(self, Removekey):
        HeadVal = self.head
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None

    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next

#Inserting at the End of the Linked List
print("===AtEnd===")
llist = SLinkedList()
llist.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

llist.head.next = e2
e2.next = e3

llist.AtEnd("Thu")

llist.LListprint()

#Inserting in between two Data Nodes
print("===Inbetween===")
llist = SLinkedList()
llist.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")

llist.head.next = e2
e2.next = e3

llist.Inbetween(llist.head.next,"Fri")

llist.LListprint()

#Removing an Item form a Liked List
print("===RemoveNode===")
llist = SLinkedList()
llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.RemoveNode("Tue")
llist.LListprint()

