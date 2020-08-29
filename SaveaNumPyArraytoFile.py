# save numpy array as csv file
'''    1. Save NumPy Array to .CSV File (ASCII) 
       2. Save NumPy Array to .NPY File (binary) 
       3. Save NumPy Array to .NPZ File (compressed) '''

# 1. Save NumPy Array to .CSV File (ASCII) 
from numpy import asarray
from numpy import savetxt
# define data
data = asarray([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
# save to csv file
savetxt('data.csv', data, delimiter=',')

# load numpy array from csv file
from numpy import loadtxt
# load array
data = loadtxt('data.csv', delimiter=',')
# print the array
print(data)

#------------------------------------------------------------------

# 2. Save NumPy Array to .NPY File (binary)
from numpy import asarray
from numpy import save
# define data
data = asarray([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
# save to npy file
save('data.npy', data)

# load numpy array from npy file
from numpy import load
# load array
data = load('data.npy')
# print the array
print(data)

#---------------------------------------------------------------------

# 3. Save NumPy Array to .NPZ File (compressed) 
from numpy import asarray
from numpy import savez_compressed
# define data
data = asarray([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
# save to npy file
savez_compressed('data.npz', data)

# load numpy array from npz file
from numpy import load
# load dict of arrays
dict_data = load('data.npz')
# extract the first array
data = dict_data['arr_0']
# print the array
print(data)
