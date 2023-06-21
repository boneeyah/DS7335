import numpy as np

# Decision Making With Matrices
# This is a pretty simple assignment.  You will do something you do everyday, but today it will be with matrix manipulations. 
# The problem is: you and your work friends are trying to decide where to go for lunch. You have to pick a restaurant that’s best for everyone.  Then you should decide if you should split into two groups so everyone is happier.  
# Despite the simplicity of the process you will need to make decisions regarding how to process the data.
# This process was thoroughly investigated in the operation research community.  This approach can prove helpful on any number of decision making problems that are currently not leveraging machine learning.  

### custom data (with the help of chatgpt)
####### user dict
users = {
    'Charlie': {'willingness to travel': 5, 'desire for new experience': 8, 'cost': 3, 'indian food': 7, 'mexican food': 5, 'hipster points': 5, 'vegetarian': 2},
    'Mac': {'willingness to travel': 6, 'desire for new experience': 8, 'cost': 5, 'indian food': 3, 'mexican food': 1, 'hipster points': 1, 'vegetarian': 1},
    'Dennis': {'willingness to travel': 4, 'desire for new experience': 2, 'cost': 4, 'indian food': 7, 'mexican food': 8, 'hipster points': 6, 'vegetarian': 4},
    'Dee': {'willingness to travel': 1, 'desire for new experience': 10, 'cost': 9, 'indian food': 7, 'mexican food': 6, 'hipster points': 6, 'vegetarian': 0},
    'Frank': {'willingness to travel': 8, 'desire for new experience': 1, 'cost': 0, 'indian food': 0, 'mexican food': 5, 'hipster points': 5, 'vegetarian': 5},
    'Artemis': {'willingness to travel': 4, 'desire for new experience': 0, 'cost': 9, 'indian food': 0, 'mexican food': 7, 'hipster points': 5, 'vegetarian': 4},
    'Cricket': {'willingness to travel': 0, 'desire for new experience': 10, 'cost': 10, 'indian food': 2, 'mexican food': 6, 'hipster points': 9, 'vegetarian': 1},
    'Artemis': {'willingness to travel': 0, 'desire for new experience': 9, 'cost': 0, 'indian food': 0, 'mexican food': 7, 'hipster points': 2, 'vegetarian': 4},
    'Carmen': {'willingness to travel': 6, 'desire for new experience': 3, 'cost': 4, 'indian food': 6, 'mexican food': 0, 'hipster points': 7, 'vegetarian': 7},
    'Zee': {'willingness to travel': 4, 'desire for new experience': 10, 'cost': 7, 'indian food': 9, 'mexican food': 1, 'hipster points': 6, 'vegetarian': 3}}

# Transform the user data into a matrix ( M_people). Keep track of column and row IDs. 
#get row names and col names
index = list(users.keys())
column_names = list(list(users.values())[0].keys())
print('column ids: {}\n row ids: {}\n'.format(column_names,index))

#build empty mat
M_people = np.zeros((len(index),len(column_names)))

#input values into matrix
for name in index:
    i = index.index(name)
    for cat in column_names:
        j = column_names.index(cat)
        M_people[i][j] = users.get(name).get(cat)
print('-------M_people matrix--------\n')
print(M_people)

# Next you collected data from an internet website. You got the following information.
restaurants  = {'Los Tacos':{'distance' : 2, 'novelty' : 1, 'cost': 7, 'average rating': 8, 'cuisine': 'Mexican', 'vegetarian': 5},
                'Char-Hut':{'distance' : 9, 'novelty' : 3, 'cost': 9, 'average rating': 9, 'cuisine': 'American', 'vegetarian': 1},
                'Brusketa':{'distance' : 9, 'novelty' : 6, 'cost': 5, 'average rating': 10, 'cuisine': 'Italian', 'vegetarian': 8},
                'Proseco 22': {'distance' : 5, 'novelty' : 9, 'cost': 3, 'average rating': 10, 'cuisine': 'Italian', 'vegetarian': 10},
                'Naz Roti':{'distance' : 3, 'novelty' : 4, 'cost': 9, 'average rating': 6, 'cuisine': 'Indian', 'vegetarian': 9},
                'Azteca':{'distance' : 7, 'novelty' : 9, 'cost': 7, 'average rating': 5, 'cuisine': 'Mexican', 'vegetarian': 7}}

r_index = list(restaurants.keys())
r_cols = list(list(users.values())[0].keys())

print('\n restaurant names: {}'.format(r_index))
# Transform the restaurant data into a matrix (M_resturants) using the same column index.
M_restaurants = np.zeros((len(r_index),len(column_names)))
for name in r_index:
    i = r_index.index(name)
    # get cuisine cat into Mexican, Indian or Neither
    if restaurants.get(name).get('cuisine') == 'Mexican':
        Mexican = 10
        Indian = 0
    elif restaurants.get(name).get('cuisine') == 'Indian':
        Indian = 10
        Mexican = 0
    else:
        Indian = 0
        Mexican = 0
    # constructing array (matrix row) within instead of rebuilding dictionary
    # array positions will match M_people columns exactly
    # really don't know how to account for hipster points without changing the formatting of either user or restaurant (will use overall rating as hipster points instead)
    M_restaurants[i] = [restaurants.get(name).get('distance'),
                        restaurants.get(name).get('novelty'),
                        restaurants.get(name).get('cost'),
                        Indian,
                        Mexican,
                        restaurants.get(name).get('average rating'),
                        restaurants.get(name).get('vegetarian')]
print('\n-----M_restaurants matrix-----\n')
print(M_restaurants)
# The most important idea in this project is the idea of a linear combination.  
# Informally describe what a linear combination is  and how it will relate to our restaurant matrix.

# Choose a person and compute(using a linear combination) the top restaurant for them.  What does each entry in the resulting vector represent?
# using Frank
A = M_people[index.index('Frank')]
comb_frank = np.sum(A*M_restaurants, axis=1)
print('\n-------Linear Combination for Frank---------\n')
print(comb_frank)
print('highest value is {}, for restaurant {}\n'.format(np.max(comb_frank),r_index[np.argmax(comb_frank)]))

# Next, compute a new matrix (M_usr_x_rest  i.e. an user by restaurant) from all people.  What does the a_ij matrix represent?
# resulting matrix will be of shape (num_users, num_restaurants)
M_usr_x_rest = np.zeros((M_people.shape[0],M_restaurants.shape[0]))
for person in index:
    #get linear combination each
    M_usr_x_rest[index.index(person)] = np.sum(M_people[index.index(person)]*M_restaurants, axis=1)
print('\n----------M_usr_x_rest----------\n')
print(M_usr_x_rest)


# Sum all columns in M_usr_x_rest to get the optimal restaurant for all users.  What do the entries represent?
totals = np.zeros(M_usr_x_rest.shape[1])
for col_index in range(M_usr_x_rest.shape[1]):
    totals[col_index] = np.sum(M_usr_x_rest.T[col_index])
print('\n------------column totals------------\n')
print(totals)
    
# Now convert each row in the M_usr_x_rest into a ranking for each user and call it M_usr_x_rest_rank.   Do the same as above to generate the optimal restaurant choice.  
M_usr_x_rest_rank = np.argsort(M_usr_x_rest)
print('\nM_usr_x_test_rank\n')
print(M_usr_x_rest_rank)

#find the optimal choice
total_rank = np.zeros(M_usr_x_rest_rank.shape[1])
for col_index in range(M_usr_x_rest_rank.shape[1]):
    total_rank[col_index] = np.sum(M_usr_x_rest_rank.T[col_index])
print('\n-------rank totals-------\n')
print(total_rank)

# Why is there a difference between the two?  What problem arrives?  What does it represent in the real world?








# Choose a person and compute(using a linear combination) the top restaurant for them.  What does each entry in the resulting vector represent? 

# Next, compute a new matrix (M_usr_x_rest  i.e. an user by restaurant) from all people.  What does the a_ij matrix represent? 

# Sum all columns in M_usr_x_rest to get the optimal restaurant for all users.  What do the entries represent?

# Now convert each row in the M_usr_x_rest into a ranking for each user and call it M_usr_x_rest_rank.   Do the same as above to generate the optimal restaurant choice.  

# Why is there a difference between the two?  What problem arrives?  What does it represent in the real world?

# How should you preprocess your data to remove this problem? 

# Find  user profiles that are problematic, explain why?

# Think of two metrics to compute the disatistifaction with the group.  

# Should you split into two groups today? 

# Ok. Now you just found out the boss is paying for the meal. How should you adjust? Now what is the best restaurant?

# Tomorrow you visit another team. You have the same restaurants and they told you their optimal ordering for restaurants. Can you find their weight matrix? 
