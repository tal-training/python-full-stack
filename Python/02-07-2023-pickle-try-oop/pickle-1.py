
import pickle 

table=[{"name":"tal", "grade":90},{"name":"gal", "grade":100},{"name":"yal", "grade":80}]

nums=[1,2,3]

with open("grades.pickle", 'wb') as f:
    pickle.dump(table, f)

with open("grades.pickle", 'rb') as f:
    loaded_table=pickle.load(f)

loaded_table[0]["grade"]=80

with open("grades.pickle", 'wb') as f:
    pickle.dump(loaded_table, f)

with open("grades.pickle", 'rb') as f:
    loaded_table=pickle.load(f)

print(loaded_table) 
