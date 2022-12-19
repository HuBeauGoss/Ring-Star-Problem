from fonctions import load_data, create_solution, CalculCost
from metaheuristiques import LocalSearch

data = load_data("data9.dat")

nom = "sol1.txt"
sol = LocalSearch(data)
create_solution(nom, sol)

print(CalculCost(data, sol), "->", sol[2])

# Data1 : 1302
# Data2 : 2308
# Data3 : 1253
# Data4 : 1765
# Data5 : 3051
# Data6 : 1767
# Data7 : 69844
# Data8 : 132268
# Data9 : 103264