import random


def hillclimbing(problem1,a):
    if(a==1):
        simple_hill(problem1)
    elif(a==2):
        stochastic_hill(problem1)
    elif(a==3):
        first_choice_hill(problem1)
    elif(a==4):
        random_restart_hill_climbing(problem1)


def simple_hill(problem1):
    a = problem1.initialstate()
    print(a.state)

    max_earn=problem1.heuristic(a)

    visitednode=0
    expandednode=0


    while(True):

        expandednode=expandednode+1

        for s1 in problem1.actions(a):
            c = problem1.result(a, s1)
            visitednode=visitednode+1

            if(problem1.heuristic(c)>max_earn):
                max_earn=problem1.heuristic(c)
                temp=c

        if(max_earn==problem1.heuristic(a)):

            print(a.state)

            print("visitenode= ",visitednode)
            print("expandenode= ",expandednode)
            print("hazine= ",-problem1.heuristic(a))

            return
        else:
            a=temp
            print(a.state)




def stochastic_hill(problem1):

    a = problem1.initialstate()
    max_earn=problem1.heuristic(a)

    print(a.state)


    visitednode=0
    expandednode=0



    while(True):

        expandednode=expandednode+1

        possible_states=[]

        for s1 in problem1.actions(a):
            c = problem1.result(a, s1)
            visitednode=visitednode+1

            if(problem1.heuristic(c)>max_earn):
                possible_states.append(c)

        if(len(possible_states)==0):
            print("visitenode= ",visitednode)
            print("expandenode= ",expandednode)
            print("hazine= ",-problem1.heuristic(a))
            print(a.state)
            return
        else:
            rand=random.randint(0,len(possible_states)-1)
            a=possible_states[rand]
            max_earn=problem1.heuristic(a)
            print(a.state)









def first_choice_hill(problem1):

    a = problem1.initialstate()
    max_earn=problem1.heuristic(a)

    print(a.state)
    print(problem1.heuristic(a))


    visitednode=0
    expandednode=0





    while(True):

        expandednode=expandednode+1


        for s1 in problem1.actions(a):
            c = problem1.result(a, s1)
            visitednode=visitednode+1


            if(problem1.heuristic(c)>max_earn):
                print(c.state)

                max_earn=problem1.heuristic(c)
                a=c
                break

        if(max_earn==problem1.heuristic(a)):

            print("visitenode= ",visitednode)
            print("expandenode= ",expandednode)
            print("hazine= ",-problem1.heuristic(a))


            print(a.state)
            return





def random_restart_hill_climbing(problem1):

    for i in range(10):
        simple_hill(problem1)










