# Homework 2
import numpy as np
from sklearn.metrics import accuracy_score # other metrics too pls!
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier # more!
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from itertools import product
import matplotlib.pyplot as plt

# adapt this code below to run your analysis
# 1. Write a function to take a list or dictionary of clfs and hypers(i.e. use logistic regression), each with 3 different sets of hyper parameters for each
# 2. Expand to include larger number of classifiers and hyperparameter settings
# 3. Find some simple data
# 4. generate matplotlib plots that will assist in identifying the optimal clf and parampters settings
# 5. Please set up your code to be run and save the results to the directory that its executed from
# 6. Investigate grid search function

M = np.loadtxt('heart.csv',delimiter=",",skiprows=1,usecols=range(0,13))
L = np.loadtxt('heart.csv',delimiter=",",skiprows=1,usecols=13)
n_folds = 5

data = (M, L, n_folds)

def run(clf_dict, data):
    M, L, n_folds = data # unpack data container
    kf = KFold(n_splits=n_folds) # Establish the cross validation
    ret = {} ####### switch back to dictionary of dictionaries # classic explication of results
    idx = 0
    for key in clf_dict.keys():
        for ids, (train_index, test_index) in enumerate(kf.split(M, L)):
        # will take the product of the hyperparameter dictionary
            prods = list(product(*clf_dict.get(key).values()))
        # run for each possible product of the hyperparameters building a new dictionary and updating
            for i in prods:
                a_dict = dict(zip(clf_dict.get(key).keys(),i))
                clf = key(**a_dict)
                clf.fit(M[train_index], L[train_index])
                pred = clf.predict(M[test_index])
                #clf_list.append(type(key()).__name__)
                #kfolds_list.append(ids)
                #params_list.append(a_dict)
                #accuracy_list.append(accuracy_score(L[test_index],pred))
                ret.update({idx:{'model':type(key()).__name__,
                     'params':a_dict,
                     'accuracy':accuracy_score(L[test_index],pred)}})
                idx +=1
    return ret

a_dict = {RandomForestClassifier:{'n_estimators':[10,100,1000],'max_depth':[1000,None],'max_features':['sqrt','log2']},
          LogisticRegression:{'penalty':['l1','l2'],'C':[.1,1,10],'solver':['liblinear','saga'],'max_iter':[6000]},
          AdaBoostClassifier:{'learning_rate':[.5,1,2],'n_estimators':[25,50,100]}}
results = run(a_dict, data)
#print(results)

for i in a_dict.keys():
    accu = []
    params = []
    for key, vals in zip(results.keys(),results.values()):
        if vals.get('model') == type(i()).__name__:
            accu.append(vals.get('accuracy'))
            params.append(key)
    print(plt.plot(params,accu))


#plt.boxplot(rf_accu)
#plt.show()





    

    


