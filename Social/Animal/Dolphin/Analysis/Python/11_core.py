# -*- coding: utf-8 -*-
"""
AFRS - Trabalho 4

Author: Gonçalo Peres
Date: 2019/02/02
"""

import networkx as nx

g=nx.read_gml('dolphins.gml')

core = nx.core_number(g)

print(core)