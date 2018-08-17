# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:43:37 2018

@author: hraanan
"""

#import community
#import networkx as nx
#
#G=nx.Graph()

out_file=open('f:/scope2/groups_scope_edges_class&folds.txt','w')
out_file.write('source\ttarget\n')
in_file=open('f:/scope2/groups_scope.txt','r')
in_file.readline()

for line in in_file:
    line=line.split('\t')
    group = line[0]
    line[1]=line[1][:-1]
    scope_list=line[1].split(';')
    for scope in scope_list:
        group = line[0]
        scope=scope[:scope.rfind('.')]
        scope=scope[:scope.rfind('.')]
        for i in range(2):
            print(group,scope)
            out_file.write(group+'\t'+scope+'\n')
            group=scope
            scope=scope[:scope.rfind('.')]
            
    
    
#    G.add_edge(line[0],line[1],whight=line[19])
#print(G.number_of_nodes())    
#nx.transitivity(G)    
#components = [comp for comp in nx.connected_components(G)]
#x=0
#for comp in components:
#    for node in list(comp):
#        out_file.write(node+'\t'+'org_'+str(x)+'\n')
#    x=x+1

print('end')

out_file.close()