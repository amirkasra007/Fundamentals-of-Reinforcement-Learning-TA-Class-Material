from randSoftMax import randsoftmax
import matplotlib.pyplot as plt
import numpy as np

#Initialization
N = 100 # Sample Size
z = [i for i in range(1,11)]  #vector z

#Random sample generation from softmax distribution on z
x = randsoftmax(z,N)[0]  

nbins = len(z)
counts, bins = np.histogram(x, nbins)
print(counts)

#True PMF of Soft-Max Distribution
y=randsoftmax(z,N)[1]

print(x)
print(y)

##Plots
# Plotting Relative Frequencies from Random Sample and True PMF in one figure
plt.title('True PMF and Relatvie frequencies comparison')
plt.stem(z, counts/N, 'r--', label='Relative Frequencies')
plt.stem(z,y,'g')
plt.grid()
plt.legend(loc = 'best')
plt.xlabel('vector z')
plt.ylabel('Intensity')
plt.show()

# Plotting Relative Frequencies from Random Sample and True PMF in seperate figures
plt.title('Relative Frequencies plot')
plt.stem(z, counts/N, 'r--', label='Relative Frequencies')
plt.grid()
plt.legend(loc = 'best')
plt.xlabel('vector z')
plt.ylabel('Intensity')
plt.show()

plt.title('True PMF plot')
plt.stem(z, y, 'g--', label='True PMF')
plt.grid()
plt.legend(loc = 'best')
plt.xlabel('vector z')
plt.ylabel('Intensity')
plt.show()
