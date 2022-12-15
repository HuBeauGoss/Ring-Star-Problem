import time, random
from fonctions import IS_Iterate, voisinage

# Recherche locale
def LocalSearch(data):

    start = time.time()
    # Temps total (Minutes * 60 secondes)
    finaltime = 0.1 * 60

    cost = float("inf")
    while(time.time()-start < finaltime):

        sol = IS_Iterate(data, 1)
        if len(sol[0]) > 3:
            for i in range(50):
                x = random.randint(1,3)
                sol = voisinage(data, sol, x)
        if sol[2] < cost:
            bestsol = sol
            cost = bestsol[2]
        
    return bestsol

# Recuit simulé
def RecSim():
    exit()