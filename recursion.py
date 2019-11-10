class node:
    def __init__(self,data):
        self.next = None
        self.data = data

class linked:
    def __init__(self):
        self.head = None

    def rev(self, link,prev):
        if link.next is None:
            self.head = link

            return
        else:
            prev = link
            self.rev(link)
            link.next = prev

    def print(self,node):
        if node.next is not None:
            print(node.daa)

link = linked()
link.head = node(7)
link.head.next = node(8)
link.head.next.next = node(9)
link.head.next.next.next = node(10)



