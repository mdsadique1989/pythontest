# This program saves a lists to a file and then loads it back

import pickle

my_list = ['apple','banana','cherry']

with open('list.pkl', 'wb') as file:
    pickle.dump(my_list,file)

with open('list.pkl', 'rb') as file:
    loaded_list = pickle.load(file)

print("Loaded List:", loaded_list)