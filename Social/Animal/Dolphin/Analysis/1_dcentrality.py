# -*- coding: utf-8 -*-
"""
AFRS - Trabalho 4

Author: Gonçalo Peres
Date: 2019/02/02
"""

import networkx as nx

g=nx.read_gml('dolphins.gml')

for i in nx.degree_centrality(g).items():
    print (i)