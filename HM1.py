from collections import Counter
import numpy as np
from itertools import combinations
import matplotlib.pyplot as plt

#### Question 2
print('\n---------------------------------------------------------------',
      '\n-----------------------   Question 2   ------------------------',
      '\n---------------------------------------------------------------')
flower_orders=['W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','B/Y','B/Y','B/Y','B/Y','B/Y','R/B/Y','R/B/Y','R/B/Y','R/B/Y','R/B/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/G','W/G','W/G','W/G','R/Y','R/Y','R/Y','R/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','W/R/B/V','W/R/B/V','W/R/B/V','W/R/B/V','W/N/R/V/Y','W/N/R/V/Y','W/N/R/V/Y','W/N/R/V/Y','N/R/Y','N/R/Y','N/R/Y','W/V/O','W/V/O','W/V/O','W/N/R/Y','W/N/R/Y','W/N/R/Y','R/B/V/Y','R/B/V/Y','R/B/V/Y','W/R/V/Y','W/R/V/Y','W/R/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/N/R/B/Y','W/N/R/B/Y','W/N/R/B/Y','R/G','R/G','B/V/Y','B/V/Y','N/B/Y','N/B/Y','W/B/Y','W/B/Y','W/N/B','W/N/B','W/N/R','W/N/R','W/N/B/Y','W/N/B/Y','W/B/V/Y','W/B/V/Y','W/N/R/B/V/Y/G/M','W/N/R/B/V/Y/G/M','B/R','N/R','V/Y','V','N/R/V','N/V/Y','R/B/O','W/B/V','W/V/Y','W/N/R/B','W/N/R/O','W/N/R/G','W/N/V/Y','W/N/Y/M','N/R/B/Y','N/B/V/Y','R/V/Y/O','W/B/V/M','W/B/V/O','N/R/B/Y/M','N/R/V/O/M','W/N/R/Y/G','N/R/B/V/Y','W/R/B/V/Y/P','W/N/R/B/Y/G','W/N/R/B/V/O/M','W/N/R/B/V/Y/M','W/N/B/V/Y/G/M','W/N/B/V/V/Y/P']

#1. Build your own counter object, then use the build-in Counter() and confirm they have the same values
# prebuilt counter
print(
    str(
    '1. Build your own counter object, then use the build-in Counter() and confirm they have the same values custom counter'
    )
)

counts_built = Counter(flower_orders)
print(str('\n------------- Prebuilt Counter -------------\n'))
print(counts_built)

#custom counter
order_count = {}
for i in flower_orders:
    a_dict = {i:flower_orders.count(i)}
    order_count.update(a_dict)
print(str('\n------------- Custom Counter -------------\n'))
print(order_count)


# 2. Count how many objects have W in them
print(
    str(
    '\n2. Count how many objects have W in them'
    )
)
W_count = [0]
for i in range(len(order_count)):
    if list(order_count.keys())[i].replace("/"," ").count("W") > 0:
        W_count = np.add(W_count, list(order_count.values())[i])

print('There are {} objects with W in them'.format(W_count.item()))

# 3. Make histogram of colors
print(
    str(
    '\n3. Make a histogram of colors'
    )
)
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

#plot colors
plt.bar(list(color_count.keys()),list(color_count.values()))
plt.title('Color Counts')
plt.show()

# 4. Rank the pairs of colors in each order regardless of how many colors are in an order
print(
    str(
    '\n4. Rank the pairs of colors in each order regardless of how many colors are in an order'
    )
)
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
print(
    str(
    '\n5. Rank the triplets of colors in each order regardless of how many colors are in an order'
    )
)
# use the previous function, with n = 3
rank3 = rank_n_order(flower_orders,3)
print(rank3)
#print(len(rank3))

# 6. Make a dictionary with key="color" and values ="waht other colors it is ordered with"
print(
    str(
    '\n6. Make a dictionary with key="color" and values = "what other colores it is ordered with"'
    )
)
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
print(co_colors)

# 7. make a graph showing the probability of having an edge between two colors based on how often they co-occur.
print(
    str(
    '\n7. Make a graph showing the probability of having an edge between two colors based on how often they co-occur'
    )
)
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

print(str('----------- values matrix -----------').center(40))
print(np.array(key_list))
print(square_matrix,'\n')
print(str('----------- probabilities matrix -----------').center(50))
print(np.round(np.divide(square_matrix,183,dtype='f'),2))

#matplotlib matrix plot
plt.matshow(square_matrix)
plt.xticks(ticks=range(10),labels=key_list)
plt.yticks(ticks=range(10),labels=key_list)
plt.title('Color Co-ocurrence Matrix')
plt.show()


#### Question 3
print('\n---------------------------------------------------------------',
      '\n-----------------------   Question 3   ------------------------',
      '\n---------------------------------------------------------------')

dead_men_tell_tales = ['Four score and seven years ago our fathers brought forth on this',
'continent a new nation, conceived in liberty and dedicated to the',
'proposition that all men are created equal. Now we are engaged in',
'a great civil war, testing whether that nation or any nation so',
'conceived and so dedicated can long endure. We are met on a great',
'battlefield of that war. We have come to dedicate a portion of',
'that field as a final resting-place for those who here gave their',
'lives that that nation might live. It is altogether fitting and',
'proper that we should do this. But in a larger sense, we cannot',
'dedicate, we cannot consecrate, we cannot hallow this ground.',
'The brave men, living and dead who struggled here have consecrated',
'it far above our poor power to add or detract. The world will',
'little note nor long remember what we say here, but it can never',
'forget what they did here. It is for us the living rather to be',
'dedicated here to the unfinished work which they who fought here',
'have thus far so nobly advanced. It is rather for us to be here',
'dedicated to the great task remaining before us--that from these',
'honored dead we take increased devotion to that cause for which',
'they gave the last full measure of devotion--that we here highly',
'resolve that these dead shall not have died in vain, that this',
'nation under God shall have a new birth of freedom, and that',
'government of the people, by the people, for the people shall',
'not perish from the earth.']

# 1. Join Everything
print(
    str(
    '\n1. Join Everything'
    )
)

join_txt = ' '.join(dead_men_tell_tales)
print(join_txt)

# 2. Remove Spaces
print(
    str(
    '\n2. Remove Spaces'
    )
)

no_spaces = join_txt.replace(' ','')
print(no_spaces)

# 3. Occurence probabilities for letters
print(
    str(
    '\n3. Occurence probabilities for letters'
    )
)
#normalize text
special = [',','.',' ','-']
join_txt = join_txt.lower()
norm_txt = []
unique_letters = []

for i in join_txt:
    if i not in special:
        norm_txt.append(i)
    if i not in unique_letters and i not in special:
        unique_letters.append(i)
norm_txt = ''.join(norm_txt)

# count 
txt_len = len(norm_txt)
letter_dict = dict()
for i in unique_letters:
    a_dict = {i:(norm_txt.count(i),np.round(norm_txt.count(i)/txt_len,2))}
    letter_dict.update(a_dict)
print('*values include count and probability\n')
print(letter_dict)

# 4. Tell me the transition probabilities for every pair of letters
print(
    str(
    '\n4. Tell me the transition probabilities for every pair of letters'
    )
)

# get all possible pairs of letters
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letter_matrix = []
trans_dict = {}
for i in alphabet:
    letter_array = []
    #letter_values = []
    for j in alphabet:
        letter_pair = i + j
        pair_count = norm_txt.count(letter_pair)
        if pair_count > 0:
            trans_prob = pair_count/norm_txt.count(i)
            trans_dict.update({i+j:np.round(trans_prob,3)})
        else:
            trans_prob = 0
        letter_array.append(trans_prob)
    letter_matrix.append(letter_array)

print('\nTransition probabilities in dictionary, with "from" and "to" letters as key-pair and probability as value')
print(trans_dict)

# 5. Make a 26x26 graph of 4. in Numpy
print(
    str(
    '\n5. Make a 26x26 graph of 4. in Numpy'
    )
)
# in addition to the dictionary, the previous nested loop saved the values for each letter in a 2D list

letter_matrix = np.asarray(letter_matrix)
np.set_printoptions(linewidth=200,precision=2)
print(alphabet)
print(letter_matrix)

# 6. Plot graph of transition probabilities from letter to letter
print(
    str(
    '\n6. Plot graph of transition probabilities from letter to letter'
    )
)

plt.matshow(letter_matrix)
plt.xticks(ticks = range(26),labels=alphabet)
plt.yticks(ticks=range(26),labels=alphabet)
plt.show()
print('"q" -> "u" has transition probability of 1, since "q" only appears once in the word "equal" ')

# 7. Flatten a Nested List
print(
    str(
    '\n7. Flatten a Nested List'
    )
)

nest_list = [[1,2,3,4,5],[26,27,28,29,30]]
flatten_list = [x for y in nest_list for x in y]
print(flatten_list)
