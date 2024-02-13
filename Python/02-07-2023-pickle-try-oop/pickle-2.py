
import pickle 

nums=[1,2]

with open("nums.pickle", 'wb') as f:
    pickle.dump(nums, f)

with open("nums.pickle", 'rb') as f:
    loaded_nums=pickle.load(f)

print(loaded_nums)