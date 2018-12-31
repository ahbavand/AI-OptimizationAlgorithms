import numpy as np
from problem import problem
from node import node
import hillclimbing
import simulated
import random



class p1(problem):
    def __init__(self):
        number_of_cities=int(input("enter number of cities"))
        self.number_of_cities=number_of_cities
        self.a = np.zeros(shape=(number_of_cities,number_of_cities))
        for i in range(0,number_of_cities):
            s=input("enter cities")
            data=s.split()
            for j in range(0,number_of_cities):
                self.a[i][j]=int(data[j])





    def initialstate(self):

        a=[]
        while len(a)<self.number_of_cities:
            l=(random.randint(0,self.number_of_cities-1))
            if(l not in a):
                a.append(l)
        y=node(a,None,1)
        return y


    def actions(self,node1):
        ac=[]
        for i in range(0,self.number_of_cities):
            for j in range(0,self.number_of_cities):
                if(i!=j):
                    a = []
                    a.append(i)
                    a.append(j)
                    ac.append(a)
        return ac


    def result(self,node1,action):

        temp=[]
        for i in range(0,self.number_of_cities):
            temp.append(node1.state[i])
        temp[int(action[0])]=node1.state[int(action[1])]
        temp[action[1]]=node1.state[action[0]]
        y=node(temp,node1,1)
        return y




    def heuristic(self,node1):
        co=0
        for i in range(0,self.number_of_cities-1):
            co=co+self.a[node1.state[i]][node1.state[i+1]]

        co=co+self.a[node1.state[self.number_of_cities-1]][node1.state[0]]

        return -co





















x=p1()
hillclimbing.hillclimbing(x,4)
#simulated.simulated(x)
