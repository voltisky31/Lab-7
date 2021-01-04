import random
tab = []
tab2 = []
tab3 = []
for i in range(0, 100):
    tab.append(random.randint(0, 10))
tup_1 = tuple(tab)
print(tup_1)
print("0 jest: ", tup_1.count(0))
print("1 jest: ", tup_1.count(1))
print("2 jest: ", tup_1.count(2))