# Calculating the canonical partition function

Now that we know how to generate all the possible microstates for a set of N spins we are in a position where we can finally calculate the canonical partition function using:

![](https://render.githubusercontent.com/render/math?math=Z=\sum_{j=1}^Me^{-\beta\E(\mathbf{x}_j)})

Remember that in this expression beta is the inverse temperature and the sum runs over the M microstates, ![](https://render.githubusercontent.com/render/math?math=\mathbf{x}_j), that the system can adopt.  H, meanwhile, is one of the Hamiltonians that we learned how to compute during the first few of these exercises.  In this particular exercise we are going to use the Hamiltonian for the 1D Ising model in an external magnetic field, H:

![](https://render.githubusercontent.com/render/math?math=E=-H\sum_{i=1}^Ns_i)

The sums here run over the number of spins, N, and the geometry is closed so ![](https://render.githubusercontent.com/render/math?math=s_{N%2B1}=s_1).

When you fill in the code in the cell on the left here the function `partitionfunction` should return the value of Z calculated by the formula above.  Within this function you will thus have a write a sum over all the possible microstates.  Notice, furthermore, that this function takes `N` (the number of spins), `H` (the magnetic field strength) and `T` (the temperature) as its input parameters. 

To compute Z you will need to compute the energy for each of the microstates that you generate.  In order to make the code more readable I have written a function called `hamiltonian` that takes the microscopic coordinates for all the spins and the magnetic field strength as its input parameters.  This function should calculate the energy for the input microstate using the Hamiltonian given above.   This function will need to be called for each of the microstates that you generate in the function called `partitionfunction`.
