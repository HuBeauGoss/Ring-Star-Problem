import time, random, copy
import numpy as np
from fonctions import IS_Iterate, FindMin, voisinage, voisinage2

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

def TabuSearch(data):

    start = time.time()
    # Temps total (Minutes * 60 secondes)
    finaltime = 0.1 * 60

    while(time.time()-start < finaltime):

        Lt_max = 100
        lt_init = 50
        tabu = []
        Sol = []
        initsol = IS_Iterate(data, 10)
        x = random.randint(1, 3)
        _, listsol = voisinage2(data, initsol, x)
        for _ in range(lt_init):
            bestsol, i = FindMin(listsol)
            tabu.append(bestsol)
            Sol.append(bestsol[2])
            listsol.pop(i)
        
        while len(tabu) < Lt_max:

            newtabu = copy.deepcopy(tabu)
            s_cur, _ = FindMin(newtabu)
            x = random.randint(1, 3)
            _, listsol = voisinage2(data, s_cur, x)
            verif = []
            for _ in range(len(listsol)):
                bestsol, i = FindMin(listsol)
                verif.append(bestsol)
                listsol.pop(i)
            
            for s_cur in verif:
                if Sol.count(s_cur[2]) == 0:
                    tabu.append(s_cur)
                    Sol.append(s_cur[2])
                    break
        
            sol, _ = FindMin(tabu)
            if (time.time()-start > finaltime):
                break
    
    return sol