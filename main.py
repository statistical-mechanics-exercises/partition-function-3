import numpy as np

def hamiltonian( spins, H ) : 
  energy = 0
  # Your code to calculate the hamiltonian goes here
  energy = -spins[0]*spins[-1] - H*spins[0]
  for i in range(1,len(spins)) : energy = energy - (spins[i-1] + H)*spins[i]
  return energy
  
def partitionfunction( N, H, T ) :
  Z = 0
  # Your code to calculate the partition function goes here
  spins = np.zeros(N)
  for index in range(2**N) : 
      for i in range(N) :
          spins[i] = np.floor( index / 2**(N-1-i) )
          index = index - spins[i]*(2**(N-1-i))
          if spins[i]==0 : spins[i] = -1
      Z = Z + np.exp( -hamiltonian(spins,H) / T )
  return Z

# Calculate the partition function for a system of 5 spins 
# with no external field at a temperature of 0.1
print( partitionfunction(5,0,0.1) )

# Calculate the paritition function for a system of 6 spins 
# with a magnetic field strength of 1 at a temperature of 0.5
print( partitionfunction(6,1,0.5) )
