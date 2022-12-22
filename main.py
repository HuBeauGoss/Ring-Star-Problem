from fonctions import load_data, create_solution, IS_Iterate, CalculCost, voisinage2
from metaheuristiques import RecSim, LS_Iterate, TabuSearch

data, nom = [], []
for i in range(9):
    data = load_data(f"data{i+1}.dat")
    # initsol = IS_Iterate(data, 1000)
    sol = TabuSearch(data)
    print(i+1, CalculCost(data, sol), "->", sol[2])
    print(100*len(sol[0])/data[0], "%")
    # nom = f"Solution {i+1}.txt"
    # create_solution(nom, sol)

""" Avant la règle du sommet 1 (dépôt) inclus dans le ring
# Data1 : 1302
# Data2 : 2272
# Data3 : 1252 (1183)
# Data4 : 1765
# Data5 : 2908
# Data6 : 1724
# Data7 : 64719
# Data8 : 126945
# Data9 : 103264
"""

    # LS_Iterate (Best) #
# Data1 : 1308
# Data2 : 2255
# Data3 : 1246
# Data4 : 1626
# Data5 : 2854
# Data6 : 1797
# Data7 : 69357
# Data8 : 130106
# Data9 : 102598

    # Recuit Simulé (30s.) #
# Data1 : 1447
# Data2 : 2413
# Data3 : 1275
# Data4 : 1827
# Data5 : 3015
# Data6 : 1835
# Data7 : 75 399
# Data8 : 139 739
# Data9 : 106 618

    # LS_Iterate (30s.) #
# Data1 : 1308
# Data2 : 2291
# Data3 : 1293
# Data4 : 1671
# Data5 : 2896
# Data6 : 1812
# Data7 : 69 588
# Data8 : 133 660
# Data9 : 104 947

""" Tabou
1// 1470
2// 2121
3// 1244
4// 1844
5// 2602
6 // 1756
7 // 78 225
8 // 121 887
9 // 97 772
"""