import pickle

# Open the pickled file in binary read mode
with open('c1p8.pickle', 'rb') as f:
    # Load the pickled data
    unpickled_data = pickle.load(f)

# Now you can work with the unpickled data
print(unpickled_data)

import matplotlib.pyplot as plt


x_values = list(unpickled_data.keys())
y_values = list(unpickled_data.values())

plt.plot(x_values, y_values)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()