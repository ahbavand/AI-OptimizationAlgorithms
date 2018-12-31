import random




def genetic(problem1):
    population=[]


    for i in range(0,50):
        population.append(problem1.random_state())

    for q in range(0,10):

#        for i in range(0, 20):
#            print(population[i].state,i)


        new_population=[]

        for i in range(0,len(population)):
            a=select(problem1,population)
            b=select(problem1,population)
            child=makechild(problem1,a,b)
            mutation(problem1,child)
            new_population.append(child)

        for i in  range(0,len(population)):
            population[i]=new_population[i]

        best=0
        worst=1000
        mean=0
        for i in range(0,len(population)):
            w=problem1.heuristic(population[i])

            if(w>best):
                best=w
            if(w<worst):
                worst=w;
            mean=mean+w

        print("best=",best)
        print("worst=",worst)
        print("mean=",mean/len(population))









def select(problem1,population):

    l=0

    for i in range(0,len(population)):
        l=l+problem1.heuristic(population[i])


    rand_number=random.randint(1,l)

    t=0
    for i in range(0,len(population)):
        t=t+problem1.heuristic(population[i])
        if(rand_number<=t):
            return population[i]
            break


def makechild(problem1,a,b):
    return problem1.cross_over(a,b)








def mutation(problem1,child):

    problem1.mutation(child)