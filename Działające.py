import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

g=nx.complete_graph(10)
a=nx.to_numpy_matrix(g)

print (a)
nx.draw(g)
plt.show()

b=np.matrix([[1,1],[0,1]])
k=nx.from_numpy_matrix(b)
nx.draw(k)


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

b=np.matrix([[0,1,1,0],[1,0,0,0],[1,1,0,1],[0,0,0,0]])
k=nx.from_numpy_matrix(b)
nx.draw(k)

plt.show()