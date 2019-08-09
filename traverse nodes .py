class node :
    def __init__(self ,d):
        self.data=d
        self.nxt=None
class LinkedList:
    def __init__(self):
        self.head=None
llob=LinkedList()
llob.head=node("mon")
n2=node("tue")
n3=node("wed")
n4=node("thu")
n5=node("fri")
llob.head.nxt=n2
n2.nxt=n3
n3.nxt=n4
n4.nxt=n5
temp=llob.head
while temp!=None:
    print(temp.data,"==>",end=' ')
    temp=temp.nxt
