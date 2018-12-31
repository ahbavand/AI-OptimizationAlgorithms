import random
import math



def simulated(problem1):



    visitednode=0
    expandednode=0



    a = problem1.initialstate()
    max_earn=problem1.heuristic(a)



    for t1 in range(1, 100):

        possible_states = []



        T=schedule(t1,3)
        if(T<=(1/1000)):
            break



        for s1 in problem1.actions(a):
            c = problem1.result(a, s1)
            possible_states.append(c)


        if(len(possible_states)==0):
            print(a.state)
            return


        else:
            rand=random.randint(0,len(possible_states)-1)

            if(problem1.heuristic(possible_states[rand])>problem1.heuristic(a)):
                a=possible_states[rand]
                expandednode=expandednode+1
                visitednode=visitednode+1


            else:

                deltaE=problem1.heuristic(possible_states[rand])-problem1.heuristic(a)
                p=random.uniform(0,1)
                if(p<(math.pow(math.e,(deltaE/T)))):
                    a=possible_states[rand]
                    expandednode=expandednode+1

                visitednode=visitednode+1







            print(a.state)

    print("visitenode= ", visitednode)
    print("expandenode= ", expandednode)
    print("hazine= ", -problem1.heuristic(a))


def schedule(t,method):
    if(method==1):
        return 100*math.pow(0.9,t)
    if(method==2):
        return 100/t
    if(method==3):
        return 100/(t*t)






