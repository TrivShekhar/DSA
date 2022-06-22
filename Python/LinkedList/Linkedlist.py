class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)
class LinkedList:
    def __init__(self):
        self.__head=None
        self.tail=None
    def insert_new_node(self,node):
        if self.__head==None:
            self.__head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def delete_node(self,data):
        if self.__head==None:
            print("List is empty")
        else:
            temp=self.__head
            if temp.data==data:
                self.__head=temp.next
                temp.next=None
            else:
                while temp.next!=None:
                    if temp.next.data==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next

    def get_head(self):
        return self.__head