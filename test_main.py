import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_partition_function(self) : 
        for k in range(1,6) :
            pfunc1, pfunc2, pfunc3 = 0, 0, 0
            for i in range(2**k) :
                num, spins = i, k*[0]
                for j in range(k) :
                    spins[j] = np.floor( num / 2**(k-1-j) )
                    num = num - spins[j]*2**(k-1-j)
                    if spins[j]==0 : spins[j] = -1
                pfunc1 = pfunc1 + np.exp( -hamiltonian( spins, 0 ) / 0.5 )
                pfunc2 = pfunc2 + np.exp( -hamiltonian( spins, 1 ) / 0.1 )
                pfunc3 = pfunc3 + np.exp( -hamiltonian( spins, -2 ) / 0.8 )
            self.assertTrue( np.abs(pfunc1-partitionfunction(k,0,0.5))<1e-7, "The function for computing the partition function is incorrect" )
            self.assertTrue( np.abs(pfunc2-partitionfunction(k,1,0.1))<1e-7, "The function for computing the partition function is incorrect" )
            self.assertTrue( np.abs(pfunc3-partitionfunction(k,-2,0.8))<1e-7, "The function for computing the partition function is incorrect" )
            
    def test_hamiltonian( self ) :
        for i in range(2**5) :
            num, spins = i, 5*[0]
            for j in range(5) :
                spins[j] = np.floor( num / 2**(4-j) )
                num = num - spins[j]*2**(4-j)
                if spins[j]==0 : spins[j] = -1
            sumspins = sum( spins )
            coup_eng = spins[0]*spins[len(spins)-1]
            for i in range(len(spins)-1) : coup_eng = coup_eng + spins[i]*spins[i+1]
            self.assertTrue( np.abs(hamiltonian( spins, 1)+coup_eng+sumspins)<1e-7, "The energies computed by the Hamiltonian are incorrect" )
            self.assertTrue( np.abs(hamiltonian( spins, -1)+coup_eng-sumspins)<1e-7, "The energies computed by the Hamiltonian are incorrect" )
            self.assertTrue( np.abs(hamiltonian( spins, 0)+coup_eng)<1e-7, "The energies computed by the Hamiltonian are incorrect" )
            self.assertTrue( np.abs(hamiltonian( spins, 2)+coup_eng+2*sumspins)<1e-7, "The energies computed by the Hamiltonian are incorrect" )
