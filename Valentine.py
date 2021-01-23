import random
from prettytable import PrettyTable

dudes = ['chinedu', 'Ewa', 'Tayo', 'Obum', 'Dami']
gals = ['Eunice', 'Queen', 'Tomi', 'Blessing', 'Ijeoma']

valentine_pair = {}

for name in dudes:
    if name not in valentine_pair.keys():
        random_gal = random.choice(gals)
        valentine_pair[name] = random_gal
        gals.remove(random_gal)
        
table = PrettyTable(['Dudes', 'Gals'])
for key, value in valentine_pair.items():
    table.add_row([key, value])
    
print(table)
# print(valentine_pair)