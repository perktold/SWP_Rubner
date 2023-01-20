#! /usr/bin/env /usr/bin/python3

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self, data=None):
        if data is not None:
            self.head = Node(data[0])
            n = self.head
            for d in data[1:]:
                n.next = Node(d)
                n.next.prev = n
                n=n.next
            self.tail=n

    def __str__(self):
        node = self.head
        out="(HEAD)<->"
        while node is not None:
            out+=str(node.data)+"<->"
            node=node.next
        return out+"(TAIL)"

    def __len__(self):
        if self.head is None:
            return 0
        n = self.head
        cnt = 1
        while n is not self.tail:
            cnt+=1
            n = n.next
        return cnt

    def insert(self, i, d):
        if i == 0:
            self.head.prev = Node(d)
            self.head.prev.next = self.head
            self.head = self.head.prev
            return

        if self.head.next is None or i >= len(self):
            self.append(d)
            return

        n=self.head
        while n is not self.tail and i > 1:
            n=n.next
            i-=1
        newnode = Node(d)
        n.next.next.prev = newnode
        newnode.next = n.next
        n.next = newnode
        newnode.prev = n

    def append(self, d):
        self.tail.next = Node(d)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

if __name__ == "__main__":
    
