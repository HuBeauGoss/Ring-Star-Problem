from fonctions import load_data, create_solution, CalculCost
from metaheuristiques import LocalSearch

data = load_data("data1.dat")

nom = "sol1.txt"
sol = LocalSearch(data)
create_solution(nom, sol)

cost = sol.pop(2)
print(CalculCost(data, sol), "->", cost)

# Data1 : 1302
# Data2 : 2308
# Data3 : 1253
# Data4 : 1765
# Data5 : 3051
# Data6 : 1767
# Data7 : 69844
# Data8 : 133204
# Data9 : 103264