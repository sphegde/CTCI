#CTCI Question 3.2


# with another stack



class minStack:
    def __init__(self):
        self.stacks=[]
        self.minStack=[]



    def push(self,value):
        if not self.minStack:

            self.minStack=[value]

        elif value < self.minStack[0]:
            self.minStack=[value]+self.minStack

        self.stacks=[value]+self.stacks

    def pop(self):

        if self.stacks[0]==self.minStack[0]:
            del self.minStack[0]
        del self.stacks[0]










ms=minStack()
ms.push(5)
ms.push(4)
ms.push(6)
ms.push(2)
print(ms.stacks)
ms.pop()

print(ms.stacks)
print(ms.minStack)
