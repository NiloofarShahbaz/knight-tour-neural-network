# knight-tour-neural-network
This is a python implementation of knight tour problem using neural networks. The algorithm is much slower than common algorithms for solving knight's tour though im my opinion it has an interesting implmentation.

several snapshots of the algorithm has been added.

for more information about the algorithm visit https://dmitrybrant.com/knights-tour.

for the **warnsdroff rule** version of knight's tour please visit https://github.com/NiloofarShahbaz/knight-tour-warnsdroff.

## Usage
- #### With GUI
    - install the requiremnts in the *requirements.txt* file.
    - you can change the **board size** in line 22 of *main.py* file.
    - run *main.py*.
- #### Without GUI
    - install numpy.
    - uncomment the 2 last lines in *knight_tour.py*(and you can change the board size).
    - run *knight_tour.py*.
    
## Output   
As Dmitry Brant mentions in his [blog](https://dmitrybrant.com/knights-tour).
> The set of degree-2 subgraphs naturally includes Hamiltonian circuits (re-entrant Knight’s Tours). However, there are many other solutions that would satisfy the network that are not knight’s tours. For example, the network could discover two or more small independent curcuits within the knight’s graph.

In this implementation the `all vertices have even degree` output indicates that a solution has been found but it may not be a knight's tour. In that case it should reinitialize all states and outputs to find another solution.
