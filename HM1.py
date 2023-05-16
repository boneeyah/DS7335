from collections import Counter
import numpy as np
from itertools import combinations
import matplotlib.pyplot as plt


flower_orders=['W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','B/Y','B/Y','B/Y','B/Y','B/Y','R/B/Y','R/B/Y','R/B/Y','R/B/Y','R/B/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/G','W/G','W/G','W/G','R/Y','R/Y','R/Y','R/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','W/R/B/V','W/R/B/V','W/R/B/V','W/R/B/V','W/N/R/V/Y','W/N/R/V/Y','W/N/R/V/Y','W/N/R/V/Y','N/R/Y','N/R/Y','N/R/Y','W/V/O','W/V/O','W/V/O','W/N/R/Y','W/N/R/Y','W/N/R/Y','R/B/V/Y','R/B/V/Y','R/B/V/Y','W/R/V/Y','W/R/V/Y','W/R/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/N/R/B/Y','W/N/R/B/Y','W/N/R/B/Y','R/G','R/G','B/V/Y','B/V/Y','N/B/Y','N/B/Y','W/B/Y','W/B/Y','W/N/B','W/N/B','W/N/R','W/N/R','W/N/B/Y','W/N/B/Y','W/B/V/Y','W/B/V/Y','W/N/R/B/V/Y/G/M','W/N/R/B/V/Y/G/M','B/R','N/R','V/Y','V','N/R/V','N/V/Y','R/B/O','W/B/V','W/V/Y','W/N/R/B','W/N/R/O','W/N/R/G','W/N/V/Y','W/N/Y/M','N/R/B/Y','N/B/V/Y','R/V/Y/O','W/B/V/M','W/B/V/O','N/R/B/Y/M','N/R/V/O/M','W/N/R/Y/G','N/R/B/V/Y','W/R/B/V/Y/P','W/N/R/B/Y/G','W/N/R/B/V/O/M','W/N/R/B/V/Y/M','W/N/B/V/Y/G/M','W/N/B/V/V/Y/P']

#1. Build your own counter object, then use the build-in Counter() and confirm they have the same values
# custom counter
order_count = {}
for i in flower_orders:
    a_dict = {i:flower_orders.count(i)}
    order_count.update(a_dict)
#print(order_count)
#prebuilt counter
counts_built = Counter(flower_orders)

# 2. Count how many objects have W in them
W_count = [0]
for i in range(len(order_count)):
    if list(order_count.keys())[i].replace("/"," ").count("W") > 0:
        W_count = np.add(W_count, list(order_count.values())[i])
#print(W_count)

# 3. Make histogram of colors
#first find all unique colors
colors = list() # using list, sorted by order of appearance
for i in flower_orders:
    a_list = list(i.replace("/"," ").split())
    for k in a_list:
        if k not in colors:
            colors.append(k)
# find counts for each color
color_count = {}
for j in colors:
    a_count = [0]
    for i in range(len(order_count)):
        if list(order_count.keys())[i].replace("/"," ").count(j)>0:
            a_count = np.add(a_count,list(order_count.values())[i])
            color_count.update({j:a_count.item()})
#print(color_count)            
# plot colors
#plt.bar(list(color_count.keys()),list(color_count.values()))
#plt.show()

# 4. Rank the pairs of colors in each order regardless of how many colors are in an order
#define function which takes the list and the number of items for each combination
def rank_n_order(input_list,n):
    color_list = list()
    full_perm = list()
  
    # iterate through each element in the list, split colors, and find combinations
    for i in input_list:
        a_list = list(i.replace("/"," ").split())
        a_perm = list(combinations(a_list,n))
        for j in a_perm:
            flip = tuple(np.flip(j))
            if flip in full_perm:
                a_perm.remove(j)
                a_perm.append(flip)
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
#print(len(rank2))

# 5. Rank the triplets of colors in each order regardless of how many colors are in an order
# use the previous function, with n = 3
rank3 = rank_n_order(flower_orders,3)
#print(rank3)
#print(len(rank3))

# 6. Make a dictionary with key="color" and values ="waht other colors it is ordered with"
#finding unique colors again for practice
key_list = []
order_colors = []
values_list = []
for i in flower_orders:
    a_color = list(i.replace("/", " ").split())
    order_colors.append(a_color)
    for j in a_color:
        if j not in key_list:
            key_list.append(j)
            a_copy = a_color.copy()
            a_copy.remove(j)
            values_list.append(a_copy)
        else:
            idx = key_list.index(j)
            a_copy = a_color.copy()
            a_copy.remove(j)
            for k in a_copy:
                if k not in values_list[idx]:
                    values_list[idx].append(k)
co_colors = dict(zip(key_list,values_list))
#print(co_colors)

# 7. make a graph showing the probability of having an edge between two colors based on how often they co-occur.
matrix = []
#iterate through color list twice to get all possible color pairs
for i in key_list:
    color_list = []
    for j in key_list:
        color_pair = [i,j]
        # getting values from the combination counter
        if tuple(color_pair) in rank2.keys():
            idx = list(rank2.keys()).index(tuple(color_pair))
            array_val = list(rank2.values())[idx]
            color_list.append(array_val)
        # getting the values for the flipped tuple
        elif tuple(np.flip(color_pair)) in rank2.keys():
            idx = list(rank2.keys()).index(tuple(np.flip(color_pair)))
            array_val = list(rank2.values())[idx]
            color_list.append(array_val)
        # setting zeroes for unseen color pairs
        else:
            color_list.append(0)
    matrix.append(color_list)
    square_matrix = np.asmatrix(matrix)
print(key_list)
print(square_matrix)