import time, random, copy
from fonctions import IS_Iterate, voisinage

# Recherche locale
def LocalSearch(data):

    start = time.time()
    # Temps total (Minutes * 60 secondes)
    finaltime = 30 * 60

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
def RecSim():
    exit()