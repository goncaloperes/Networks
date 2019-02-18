# -*- coding: utf-8 -*-
"""
AFRS - Trabalho 4

Author: Gonçalo Peres
Date: 2019/02/02
"""

import networkx as nx

g=nx.read_gml('dolphins.gml')

for i in nx.pagerank(g, alpha=0.85).items():
    print (i)