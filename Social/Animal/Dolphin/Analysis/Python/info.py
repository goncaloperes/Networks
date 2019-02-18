# -*- coding: utf-8 -*-
"""
AFRS - Trabalho 4

Author: Gonçalo Peres
Date: 2019/02/02
"""

import networkx as nx
import matplotlib.pyplot as plt

g=nx.read_gml('dolphins.gml')

print (nx.info(g))

print (nx.is_directed(g))

#Grafo - Figura 10 
nx.draw(g)
plt.show()

#Grafo - Figura 12 
nx.draw(g, node_color = "blue", with_labels=True)
plt.show()