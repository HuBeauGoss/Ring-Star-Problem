import time, random, copy
import numpy as np
from fonctions import IS_Iterate, voisinage

# Recherche locale
def LocalSearch(data):

    start = time.time()
    # Temps total (Minutes * 60 secondes)
    finaltime = 0.5 * 60

    cost = float("inf")
    while(time.time()-start < finaltime):

        sol = IS_Iterate(data, 1000)
        if len(sol[0]) > 3:
            for i in range(50):
                x = random.randint(1,3)
                sol = voisinage(data, sol, x)
                if sol[2] < cost:
                    bestsol = copy.deepcopy(sol)
                    cost = bestsol[2]
        print(cost)
    return bestsol

# Recuit simulé
def RecSim(data):

    start = time.time()
    # Temps total (Minutes * 60 secondes)
    finaltime = 0.5 * 60

    bestcost = float("inf")
    while(time.time()-start < finaltime):

        T = 100
        Tf = 0.001
        coeff = 0.95
        sol = IS_Iterate(data, 100)
        cost = sol[2]
        while T > Tf:

            if len(sol[0]) > 3:
                for _ in range(10):
                    x = random.randint(1,3)
                    newsol = voisinage(data, sol, x)
                    delta = newsol[2] - cost
                    if delta < 0:
                        sol = newsol
                        cost = sol[2]
                    else:
                        p = np.exp(-delta/T)
                        if random.random() < p:
                            sol = newsol
                            cost = sol[2]
            T *= coeff
            if sol[2] < bestcost:
                bestsol = sol
                bestcost = bestsol[2]
        
    return bestsol