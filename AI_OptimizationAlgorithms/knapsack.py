import numpy as np
from problem import problem
from node import node
import genetic
import random


class p2(problem):


    def __init__(self):
        number = int(input("enter number of knapsak"))
        self.number=number
        self.waights = np.zeros(shape=(number))
        self.values=np.zeros(shape=(number))
        s = input("enter waights")
        data=s.split()
        for i in range(0,number):
            self.waights[i]=int(data[i])
        f = input("enter values")
        data=f.split()
        for i in range(0,number):
            self.values[i]=int(data[i])
        capasity = int(input("enter capasity of knapsak"))
        self.capasity=capasity


    def random_state(self):
        a=[]
        for i in range(0,self.number):
            r=random.randint(0,1)
            a.append(r)

        y=node(a,None,1)

        return y


    def heuristic(self,node1):
        h=0
        w=0
        for i in range(0,self.number):
            if((node1.state)[i]==1):
                h=h+self.values[i]
                w=w+self.waights[i]
        if(w>self.capasity):
            return 1
        else:
            return h


    def cross_over(self,node1,node2):
        new=[]
        n=1
        s=set()
        while len(s)<n:
            s.add(random.randint(1,self.number-2))

        a=list(s)

        r=0

        for i in range(0,self.number):
            if(i in a ):
                r=r+1
            if((r%2)==0):
                new.append((node1.state)[i])

            else:
                new.append((node2.state)[i])

        y = node(new, None, 1)

        return y


    def mutation(self,node1):
        p=(1/(self.number*40))
        a=[]
        for i in range(0,self.number):
            a.append((node1.state)[i])
        for i in range(0,self.number):
            ran=random.uniform(0,1)
            if(ran<(1/p)):
                if(a[i]==0):
                    a[i]=1
                else:
                    a[i]=0
        y = node(a, None, 1)
        return y





x=p2()


genetic.genetic(x)




