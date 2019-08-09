class node:
    def __init__(self,x):
        self.data=x
        self.add=None
n1=node(500)
n2=node(100)
n3=node(200)
n4=node(300)
n5=node(400)
n2.add=n4
n4.add=n5
n5.add=n3
n3.add=n1
temp=n2
while temp!=None:
    print(temp.data,"==>",end=' ')
    temp=temp.add
