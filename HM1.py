from collections import Counter
import numpy as np
from itertools import combinations
import matplotlib.pyplot as plt


flower_orders=['W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','B/Y','B/Y','B/Y','B/Y','B/Y','R/B/Y','R/B/Y','R/B/Y','R/B/Y','R/B/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/G','W/G','W/G','W/G','R/Y','R/Y','R/Y','R/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','W/R/B/V','W/R/B/V','W/R/B/V','W/R/B/V','W/N/R/V/Y','W/N/R/V/Y','W/N/R/V/Y','W/N/R/V/Y','N/R/Y','N/R/Y','N/R/Y','W/V/O','W/V/O','W/V/O','W/N/R/Y','W/N/R/Y','W/N/R/Y','R/B/V/Y','R/B/V/Y','R/B/V/Y','W/R/V/Y','W/R/V/Y','W/R/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/N/R/B/Y','W/N/R/B/Y','W/N/R/B/Y','R/G','R/G','B/V/Y','B/V/Y','N/B/Y','N/B/Y','W/B/Y','W/B/Y','W/N/B','W/N/B','W/N/R','W/N/R','W/N/B/Y','W/N/B/Y','W/B/V/Y','W/B/V/Y','W/N/R/B/V/Y/G/M','W/N/R/B/V/Y/G/M','B/R','N/R','V/Y','V','N/R/V','N/V/Y','R/B/O','W/B/V','W/V/Y','W/N/R/B','W/N/R/O','W/N/R/G','W/N/V/Y','W/N/Y/M','N/R/B/Y','N/B/V/Y','R/V/Y/O','W/B/V/M','W/B/V/O','N/R/B/Y/M','N/R/V/O/M','W/N/R/Y/G','N/R/B/V/Y','W/R/B/V/Y/P','W/N/R/B/Y/G','W/N/R/B/V/O/M','W/N/R/B/V/Y/M','W/N/B/V/Y/G/M','W/N/B/V/V/Y/P']
#prebuilt counter
counts_built = Counter(flower_orders)

# custom counter
order_count = {}
for i in flower_orders:
    a_dict = {i:flower_orders.count(i)}
    order_count.update(a_dict)

# count how many orders have W
W_count = [0]
for i in range(len(order_count)):
    if list(order_count.keys())[i].replace("/"," ").count("W") > 0:
        W_count = np.add(W_count, list(order_count.values())[i])
print(W_count)

# plot color counts
#first find all unique colors
colors = set() # using set, no set order since sets are not sorted
for i in range(len(flower_orders)):
    for j in flower_orders[i]:
        a_set = set(j.replace("/"," ").split())
        colors = colors.union(a_set)
print(colors)

# plot color counts
#first find all unique colors
colors = list() # using list, sorted by order of appearance
for i in flower_orders:
    a_list = list(i.replace("/"," ").split())
    for k in a_list:
        if k not in colors:
            colors.append(k)
print(colors)

# find counts for each color
color_count = {}
for j in colors:
    a_count = [0]
    for i in range(len(order_count)):
        if list(order_count.keys())[i].replace("/"," ").count(j)>0:
            a_count = np.add(a_count,list(order_count.values())[i])
            color_count.update({j:a_count.item()})
print(color_count)            

# plot colors
plt.bar(list(color_count.keys()),list(color_count.values()))
plt.show()


def rank_n_order(input_list,n):
    color_list = list()
    full_perm = list()
    
    # iterate through each element in the list, split colors, and find combinations
    for i in input_list:
        a_list = list(i.replace("/"," ").split())
        a_perm = list(combinations(a_list,n))
        full_perm.extend(a_perm)
        for k in a_list:
            if k not in color_list:
                color_list.append(k)

    #create a dictionary with each possible combination 
    color_dict = {}
    for i in full_perm:
        a_dict = {i:full_perm.count(i)}
        color_dict.update(a_dict)
    return(dict(
        sorted(
            color_dict.items(),
            key = lambda x:x[1],
            reverse=True
    )
    )
    )

rank2 = rank_n_order(flower_orders,2)
print(rank2)
print(len(rank2))
            
rank3 = rank_n_order(flower_orders,3)
print(rank3)
print(len(rank3))