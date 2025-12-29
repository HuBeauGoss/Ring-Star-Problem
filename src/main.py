from functions import load_data, IS_Iterate, CalculCost, create_solution
from metaheuristics import LS_Iterate, RecSim, TabuSearch

data, nom = [], []
for i in range(9):
    data = load_data(f"data/data{i+1}.dat")
    initsol = IS_Iterate(data, 1000)
    sol = TabuSearch(data)
    print(f"[DEBUG] {i+1}. | Cost = {CalculCost(data, sol)} | Solution :\n\t{sol[2]}")
    # print(f"{100 * len(sol[0]) / data[0]} %")
    nom = f"Solution {i+1}.txt"
    create_solution(nom, sol)
