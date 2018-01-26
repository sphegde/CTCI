#ctci q 3.6
import collections


class pet:
    def __init__(self,name,doi,type):
        self.name=name
        self.doi=doi
        self.type=type

class shelter:
    def __init__(self):
        self.dogs=list()
        self.cats=list()
        self.order=0

    def enqueueDogs(self,name,type):
         dog=pet(name,self.order,"dog")
         self.dogs.append(dog)
         self.order=self.order+1
         return self.dogs


    def enqueueCats(self,name,type):
         cat=pet(name,self.order,"cat")
         self.cats.append(cat)
         self.order=self.order+1
         return self.cats

    def dequeueDogs(self):
        del self.dogs[0]
    def dequeueCats(self):
        del self.cats[0]
    def dequeueAny(self):
        if self.dogs[0].doi < self.cats[0].doi:
            del self.dogs[0]
        else:
            del self.cats[0]



s=shelter()
s.enqueueCats("cat1","cat")
s.enqueueCats("cat2","cat")
s.enqueueDogs("pup1","dog")
s.enqueueDogs("pup2","dog")
s.dequeueAny()
for i in s.dogs:
    print(i.type)

for i in s.cats:
    print(i.type)









