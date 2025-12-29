from fonctions import load_data, create_solution, IS_Iterate, CalculCost, voisinage2
from metaheuristiques import RecSim, LS_Iterate, TabuSearch

data, nom = [], []
for i in range(9):
    data = load_data(f"Data/data{i+1}.dat")
    initsol = IS_Iterate(data, 1000)
    sol = TabuSearch(data)
    # print(i+1, CalculCost(data, sol), "->", sol[2])
    # print(f"{100 * len(sol[0]) / data[0]} %")
    nom = f"Solution {i+1}.txt"
    create_solution(nom, sol)
    
