import time, random, copy
import numpy as np
from fonctions import IS_Iterate, voisinage

# Recherche locale
def LocalSearch(data, sol):

    start = time.time()
    # Temps total (Minutes * 60 secondes)
    finaltime = 0.02 * 60

    bestsol = copy.deepcopy(sol)
    while(time.time()-start < finaltime):

        if len(sol[0]) > 3:
            for _ in range(50):
                x = random.randint(1,3)
                sol = voisinage(data, sol, x)
                if sol[2] < bestsol[2]:
                    bestsol = copy.deepcopy(sol)
                    # print("LS :", bestsol[2])
        sol = IS_Iterate(data, random.randint(1, 100))

    return bestsol

# Recuit simulé
def RecSim(data, sol):
    
    start = time.time()
    # Temps total (Minutes * 60 secondes)
    finaltime = 0.5 * 60

    bestsol = copy.deepcopy(sol)
    while(time.time()-start < finaltime):

        T = random.randint(50, 300)
        Tf = random.random() * random.randint(1, 3)
        coeff = random.randint(50, 90) / 100
        while T > Tf:

            if len(sol[0]) > 3:
                for _ in range(10):
                    x = random.randint(1, 3)
                    newsol = voisinage(data, sol, x)
                    delta = newsol[2] - sol[2]
                    if delta < 0:
                        sol = newsol.copy()
                        if sol[2] < bestsol[2]:
                            bestsol = copy.deepcopy(sol)
                    else:
                        p = np.exp(-delta/T)
                        if random.random() < p:
                            sol = newsol.copy()
            T *= coeff
        sol = IS_Iterate(data, 1).copy()
        
    return bestsol

def LS_Iterate(data):

    start = time.time()
    # Temps total (Minutes * 60 secondes)
    finaltime = 0.1 * 60
    
    temp = float("inf")
    while(time.time()-start < finaltime):

        sol = IS_Iterate(data, 1)
        sol = LocalSearch(data, sol)
        cost = sol[2]
        if cost < temp:
            temp = cost
            save = sol.copy()
    
    return save