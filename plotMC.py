import re
import matplotlib.pyplot as plt
import numpy as np

N = 1000000
data = [[],[],[],[]]
k = [[],[],[],[]]
i = -1

with open('expected_values.txt', 'r') as file:
    for line in file.readlines():
        if re.match('probability: [0-9]*',line):
            i+=1
            pass
        # Split the line on the comma
        else:
            parts = line.split(',')
            k[i].append(int(parts[0].split(':')[1]))
            data[i].append(float(parts[1].split(':')[1].replace('\n', '')))
            

# Create a figure with four subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot the data on each subplot
axs[0, 0].plot(k[0], data[0], 'k-')                     
axs[0, 0].set_xlim(min(k[0]), max(k[0]))
axs[0, 0].set_ylim(min(data[0])/2, max(data[0])*1.8)

axs[0, 1].plot(k[1], data[1], 'g-')                 
axs[0, 1].set_xlim(min(k[1]), max(k[1]))      
axs[0, 1].set_ylim(min(data[1])/2, max(data[1])*1.8)

axs[1, 0].plot(k[2], data[2], 'b-')                 
axs[1, 0].set_xlim(min(k[2]), max(k[2]))      
axs[1, 0].set_ylim(min(data[2])/2, max(data[2])*1.8)

axs[1, 1].plot(k[3], data[3], 'r-')                 
axs[1, 1].set_xlim(min(k[3]), max(k[3]))      
axs[1, 1].set_ylim(min(data[3])/2, max(data[3]))

# Set titles and labels for the subplots
axs[0, 0].set_title('P = 0.1')
#axs[0, 0].set_xlabel('k')
axs[0, 0].set_ylabel('exp_tests')

axs[0, 1].set_title('P = 0.01')
#axs[0, 1].set_xlabel('k')
axs[0, 1].set_ylabel('exp_tests')

axs[1, 0].set_title('P = 0.001')
axs[1, 0].set_xlabel('k')
axs[1, 0].set_ylabel('exp_tests')

axs[1, 1].set_title('P = 0.0001')
axs[1, 1].set_xlabel('k')
axs[1, 1].set_ylabel('exp_tests')

# Display the figure
#plt.show()
plt.savefig("plots/exp_tests_MC.png")

#-----------------------------------------------------------plot for the exp reduce workload
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
data = [[(N-val)*100/N for val in row] for row in data]

# Plot the data on each subplot
axs[0, 0].plot(k[0], data[0], 'k-')                     
axs[0, 0].set_xlim(min(k[0]), max(k[0]))
axs[0, 0].set_ylim(0, max(data[0]) + 10)

axs[0, 1].plot(k[1], data[1], 'g-')                 
axs[0, 1].set_xlim(min(k[1]), max(k[1]))      
axs[0, 1].set_ylim(0, max(data[1]) + 10)

axs[1, 0].plot(k[2], data[2], 'b-')                 
axs[1, 0].set_xlim(min(k[2]), max(k[2]))      
axs[1, 0].set_ylim(0, max(data[2]) + 10)

axs[1, 1].plot(k[3], data[3], 'r-')                 
axs[1, 1].set_xlim(min(k[3]), max(k[3]))      
axs[1, 1].set_ylim(0, max(data[3]) + 10)

# Set titles and labels for the subplots
axs[0, 0].set_title('P = 0.1')
#axs[0, 0].set_xlabel('k')
axs[0, 0].set_ylabel('exp_reduce')

axs[0, 1].set_title('P = 0.01')
#axs[0, 1].set_xlabel('k')
axs[0, 1].set_ylabel('exp_reduce')

axs[1, 0].set_title('P = 0.001')
axs[1, 0].set_xlabel('k')
axs[1, 0].set_ylabel('exp_reduce')

axs[1, 1].set_title('P = 0.0001')
axs[1, 1].set_xlabel('k')
axs[1, 1].set_ylabel('exp_reduce')

# Display the figure
#plt.show()
plt.savefig("plots/exp_reduce_MC.png")
