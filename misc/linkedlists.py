#linkedlist implementation

class node():
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

    def insert_front(self,value):
        temp=node(value)
        temp.next=self.head
        self.head=temp

    def reverseIterative(self):
        current=self.head
        temp = None
        prev= None
        while(current):
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        self.head=prev

    # reverse recursive

    def add_behind(self,value):
        temp=self.head
        while(temp.next):
            temp=temp.next
        new_node=node(value)
        temp.next=new_node



    #Question 1
    def remove_duplicates(self):
        table={}
        current=self.head
        count=0
        prev=self.head
        while(current):
            if(current.data in table):
                prev.next=current.next
            else:
                table[current.data]=count
                prev=current
                count=count+1
            current=current.next



    #Question 1 (alternative)
    def remove_duplicates_runners(self):
        current=self.head
        while(current):
            runner = current
            while(runner.next):
                if(current.data==runner.next.data):
                    runner.next=runner.next.next

                else:
                    runner=runner.next

            current=current.next

    #Question 2
    def kth_node(self,k):
        ptr1=ptr2=self.head

        for i in range(k):
            if ptr2==None:
                return None
            ptr2=ptr2.next

        while(ptr2):
            ptr2=ptr2.next
            ptr1=ptr1.next
        return ptr1.data

    #Question 4




    def value_at_position(self,pos):
        temp=self.head
        count=1
        while(count<pos):
            count+=1
            temp=temp.next
        print(temp.data)



    def printL(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next


l=LinkedList()
l.insert_front(4)
l.insert_front(3)
l.insert_front(5)
l.insert_front(2)
l.insert_front(1)
l.add_behind(5)
print("linked list printed")
l.printL()
print("kth node from behind")
print(l.kth_node(2))
print("value at")
l.value_at_position(4)
print("remove duplicates")
l.remove_duplicates_runners()
l.printL()
print("reversed list")
l.reverseIterative()
l.printL()








